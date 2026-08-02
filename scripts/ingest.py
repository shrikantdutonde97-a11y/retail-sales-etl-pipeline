import pandas as pd
from pathlib import Path

def extract_data():
    """
    Read all CSV files from the raw folder.
    Returns a dictionary:
    {
        "filename.csv": dataframe
    }
    """

    project_root = Path(__file__).resolve().parent.parent
    raw_data_path = project_root / "data" / "raw"

    csv_files = list(raw_data_path.glob("*.csv"))

    dataframes = {}

    for file in csv_files:
        df = pd.read_csv(file)
        dataframes[file.name] = df

    return dataframes

if __name__ == "__main__":
    data = extract_data()

    for filename, df in data.items():
        print(f"{filename} -> {df.shape}")