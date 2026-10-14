# Decisions log
Every cleaning/ modeling choice will be recorded here; what I decided, why, and what it affected.

## Data Source
- Using the exploratory file only (upworthy-archive-exploratory-packages-03.12.2020.csv). The confirmatory file stays untouched until the final run.
- Since this version has no randomization flag column, I will derive it from the documented window, 2013-06-25 to 2014-01-10.

## Step 2 results
Output of src/clean.py run 2026-10-13, March 2020 exploratory file.

- Raw: 22,666 packages, 4,873 tests
- Validity checks: all zero (no non-positive impressions, negative clicks, clicks above impressions, duplicate rows, or missing test IDs or dates)
- Flagged ('problem' = 1): 4,278 packages, 1,050 tests. Derived from dates, not the archive's official 'problem' column
- Kept ('problem' = 0): 18,388 packages, 3,823 tests.

Note: an earlier count gave 18,411 clean packages, 23 more than above. Its still unresolved. Should be compared with the official 'problem' column which I could not find. 






Note: Flag uses UTC and as a result using a different time zone would move a handful of tests at the window edges.

## EDA Tentative goal
- Check packages per tests
    - check whether tests have the same number of packages

- Impressions per package
    - check sample sizes, small sample --> noisy click rates 
- click rate per package distribution
- impression balance within tests
    -  to make sure the impressions were shown about equally often
- audit memo: any data quality concerns there I encounter?

* we only do it with 'problem' == 0 since those are the ones used 

