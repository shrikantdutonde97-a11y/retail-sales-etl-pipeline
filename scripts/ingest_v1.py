import pandas as pd
from pathlib import Path

# Project root folder
project_root = Path(__file__).resolve().parent.parent

# Path to the raw data folder
raw_data_path = project_root / "data" / "raw"

print(raw_data_path)

# Find all CSV files in the raw folder
csv_files = list(raw_data_path.glob("*.csv"))

print(csv_files)

# Read every CSV file
for file in csv_files:
    df = pd.read_csv(file)

    # Transform Date column from object to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    print(f"\nFile Name: {file.name}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nSummary Statistics:")
    print(df.describe())

    # Save transformed data
processed_path = project_root / "data" / "processed" / file.name

df.to_csv(processed_path, index=False)

print(f"\nProcessed file saved to: {processed_path}")