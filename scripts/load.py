from logger import setup_logger
from pathlib import Path

def load_data(dataframes):
    """
    Save transformed DataFrames to the processed folder.
    """
    logger = setup_logger()

    project_root = Path(__file__).resolve().parent.parent
    processed_path = project_root / "data" / "processed"

    for filename, df in dataframes.items():

        output_file = processed_path / filename

        df.to_csv(output_file, index=False)

        logger.info(f"Saved: {output_file}")


from ingest import extract_data
from transform import transform_data

if __name__ == "__main__":

    data = extract_data()

    transformed_data = transform_data(data)

    load_data(transformed_data)        