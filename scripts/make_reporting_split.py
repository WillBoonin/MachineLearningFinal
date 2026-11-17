"""
Create the 20% REPORTING set (held out, untouched until the final phase)
and the 80% development set from the UCI Phishing Websites dataset.

Usage (from repo root):
    python scripts/make_reporting_split.py

Downloads the original data from UCI, converts ARFF -> CSV, drops exact
duplicate rows, and does a stratified 80/20 split with a fixed random seed so it is reproducible.
"""
import io
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

URL = "https://archive.ics.uci.edu/static/public/327/phishing+websites.zip"
SEED = 4021
DATA = Path(__file__).resolve().parent.parent / "Data"


def load_arff(text: str) -> pd.DataFrame:
    cols, rows, in_data = [], [], False
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("%"):
            continue
        low = line.lower()
        if low.startswith("@attribute"):
            cols.append(line.split()[1])
        elif low.startswith("@data"):
            in_data = True
        elif in_data:
            rows.append([int(v) for v in line.split(",")])
    return pd.DataFrame(rows, columns=cols)


def main():
    DATA.mkdir(exist_ok=True)
    raw = urllib.request.urlopen(URL).read()
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        text = z.read("Training Dataset.arff").decode("utf-8")
    df = load_arff(text)
    print(f"Loaded {df.shape[0]} rows x {df.shape[1]} columns")

    # ~47% of rows are exact duplicates (features + label). If we split
    # without removing them, most reporting rows also appear in the
    # development set and the final evaluation is leaked/inflated.
    df = df.drop_duplicates().reset_index(drop=True)
    print(f"After removing exact duplicates: {len(df)} rows")

    dev, report = train_test_split(
        df, test_size=0.20, stratify=df["Result"], random_state=SEED
    )
    report.to_csv(DATA / "reporting_set.csv", index=False)
    dev.to_csv(DATA / "development_set.csv", index=False)
    print(f"Development set: {len(dev)} rows -> Data/development_set.csv")
    print(f"Reporting set:   {len(report)} rows -> Data/reporting_set.csv (DO NOT TOUCH)")


if __name__ == "__main__":
    main()
