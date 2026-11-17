# Phishing Website Detection at a Fixed False-Positive Rate

DS 4021 Final Project

## Research question
Which model (SVM, random forest, or neural network) detects phishing websites most effectively when the false-positive rate is held fixed, and how much performance is kept with a small, interpretable feature subset?

## Data
- Source: UCI Machine Learning Repository, *Phishing Websites* (id 327): https://archive.ics.uci.edu/dataset/327/phishing+websites
- `Data/reporting_set.csv`: 20% stratified hold-out. **Do not open, explore, or train on it until the final evaluation.**
- `Data/development_set.csv`: 80% used for all exploration, tuning, and cross-validation.
- The original 11,055 rows contain 5,206 exact duplicates; these are dropped before splitting (5,849 unique rows) so the reporting set does not overlap the development set.
- Recreate both with `python scripts/make_reporting_split.py` (seed 4021).

## Layout
```
Data/        reporting + development sets
scripts/     data prep scripts
notebooks/   analysis notebooks
```
