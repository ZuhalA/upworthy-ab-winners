from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = ROOT / "data" / "raw" / "upworthy-archive-exploratory-packages-03.12.2020 (1).csv"
OUT_PATH = ROOT / "data" / "clean" / "upworthy-archive-exploratory-packages-03.12.2020 (1).csv"

# Window of the time which is suspected to have randomization issue according to the archives documentation. End date is inclusive
WINDOW_START = "2013-06-25"
WINDOW_END = "2014-01-10"

def load_raw(path):
    df = pd.read_csv(path)
    return df.drop(columns=["Unnamed: 0"], errors="ignore")

def parse_dates(df):
    df = df.copy()
    df["created_at"] = pd.to_datetime(df["created_at"], format="ISO8601", utc=True)
    return df

def check_validity(df):
    #report problems - no drop, just a dict of counts
    issues = {
        "impressions <= 0": int((df["impressions"] <= 0).sum()),
        "clicks < 0": int((df["clicks"] < 0).sum()),
        "clicks > impressions": int((df["clicks"] > df["impressions"]).sum()),
        "duplicate rows": int(df.duplicated().sum()),
        "missing test id": int(df["clickability_test_id"].isna().sum()),
        "missing created_at": int(df["created_at"].isna().sum()),        
    }
    for name, count in issues.items():
        print(f"validity | {name}: {count}")
    return issues
    
def add_test_start(df):
    """Date each test according to its first package created_at"""
    df = df.copy()
    df["test_start"] = df.groupby("clickability_test_id")["created_at"].transform("min")
    return df

def add_randomization_flag(df, start, end):
    #problem =1 if between 00:00 - 23:59:59 , else 0
    df = df.copy()
    lo = pd.Timestamp(start, tz="UTC")
    hi = pd.Timestamp(end, tz="UTC") + pd.Timedelta(days=1)
    df["problem"] = ((df["test_start"] >= lo) & (df["test_start"] < hi)).astype(int)
    return df

def summarize(df, label):
    n_tests = df["clickability_test_id"].nunique()
    print(f"{label}: {len(df):,} packages, {n_tests:,} tests")

def main():
    df = load_raw(RAW_PATH)
    summarize(df, "raw")
    
    df = parse_dates(df)
    check_validity(df)
    
    df = add_test_start(df)
    df = add_randomization_flag(df, WINDOW_START, WINDOW_END)

    summarize(df[df["problem"] == 1], "flagged (problem=1)")
    summarize(df[df["problem"] == 0], "kept (problem=0)")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)
    print(f"wrote {OUT_PATH}")

if __name__ == "__main__":
    main()