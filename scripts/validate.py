from logger import setup_logger

def validate_data(dataframes):
    """
    Validate each DataFrame in the dictionary.
    """
    logger = setup_logger()

    for filename, df in dataframes.items():

        logger.info("=" * 50)
        logger.info(f"Validating: {filename}")
        logger.info("=" * 50)

        logger.info(f"Column Names: {df.columns.tolist()}")

        logger.info(f"\nData Types:\n{df.dtypes}")

        logger.info(f"\nMissing Values:\n{df.isnull().sum()}")

        logger.info(f"Duplicate Rows: {df.duplicated().sum()}")

from ingest import extract_data

if __name__ == "__main__":
    data = extract_data()
    validate_data(data)