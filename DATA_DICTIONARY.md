# Data dictionary

Source: Upworthy Research Archive, exploratory file `upworthy-archive-exploratory-packages-03.12.2020.csv` (March 2020 release).

One row is one package (a headline and image bundle) inside one test. The file holds aggregate impressions and clicks per package only: no visitor level data, and no image files. This release has no `problem` column, so the randomization flag is derived from dates (see DECISIONS.md).

Tags: **Use** = needed for the analysis, **Maybe** = might use later, **Ignore** = not used.

## Columns

- `Unnamed: 0` [Ignore]: an artifact of how the file was saved. Values are the same as the row index.
- `created_at` [Use]: date and time the package was created. The time zone is unknown. Needed for each test's start date and the randomization flag.
- `updated_at` [Ignore]: the last time the package was updated in the Upworthy system.
- `clickability_test_id` [Use]: the unique ID of a test. Each test contains packages that were randomly assigned to viewers.
- `excerpt` [Ignore]: a one-sentence excerpt of the article.
- `headline` [Maybe]: the headline shown to viewers. It is one of the stimuli being tested.
- `lede` [Ignore]: the opening sentence or paragraph of the story.
- `slug` [Ignore]: the internal part of the web address.
- `eyecatcher_id` [Maybe]: the image ID. Packages with the same image share an ID. The image files are not available.
- `impressions` [Use]: the number of viewers randomly assigned to this package. A test's total participants is the sum of impressions over all packages with the same `clickability_test_id`.
- `clicks` [Use]: the number of those viewers who clicked on the package. Click rate = clicks / impressions.
- `significance` [Ignore]: shown to editors to guide decisions. It is not a statistical significance result, and I don't know its method.
- `first_place` [Ignore]: shown to editors, along with `significance`, to guide which package to choose.
- `winner` [Ignore]: whether editors selected the package for the Upworthy site after the test. This is an editor decision, not a statistical result. Our own selected package will be named something else.
- `share_text` [Ignore]: a summary for display on social media when the article is shared. It was not shown in tests, which ran on the Upworthy website.
- `square` [Ignore]: when used, part of the same social media sharing suggestion as `share_text`.
- `test_week` [Use]: the week the package was created, a variable built by the archive creators for stratified random sampling. Useful for time coverage.

## Data quality notes

(Will fill after the EDA: missing values, inconsistent formats, and anything unexpected.)


