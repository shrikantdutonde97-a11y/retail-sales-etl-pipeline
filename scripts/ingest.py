from logger import setup_logger
import pandas as pd
from pathlib import Path
from config import RAW_DATA_PATH

def extract_data():

    logger = setup_logger()

    #project_root = Path(__file__).resolve().parent.parent
    #raw_data_path = project_root / "data" / "raw"

    csv_files = list(RAW_DATA_PATH.glob("*.csv"))

    dataframes = {}

    for file in csv_files:

        logger.info(f"Reading file: {file.name}")

        try:
            df = pd.read_csv(file)

            logger.info(
                f"Loaded {file.name} with {df.shape[0]} rows and {df.shape[1]} columns"
            )

            dataframes[file.name] = df

        except Exception as e:
            logger.error(f"Failed to read {file.name}: {e}")

    return dataframes

if __name__ == "__main__":
    data = extract_data()

    for filename, df in data.items():
        print(f"{filename} -> {df.shape}")