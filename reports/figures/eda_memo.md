## EDA memo: Upworthy exploratory file

## Data looks like this:
- Each tests have 2-14 packages (median = 5)
- Median package got 3,118 impressions and 13 got under 1,000
- median CTR = 1.11% and its right skewed (mean 1.36%). Noise per package ~ 0.19 pp

## Things to keep in mind:
- Zero clicks: 10 packahes & one whole test. (Kept)
- SRM: 18 / 3,823 tests fail p < 0.001 which is like 83 packaegs. They are flagged as `srm_fail` and kept them.
- Built `problem` flag from the archives dates because I couldn't find the dataest with official column.

## Desicion based in these findings
In Winner Curse analysis part of project we will use per test prior mean.
- What the per-test center does?
    - Shrinkage pulls each package’s measured rate toward a center. Per test center measures each package against its own test, so the shrinkage only corrects the within test lead.