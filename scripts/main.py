from ingest import extract_data
from validate import validate_data
from transform import transform_data
from load import load_data
from logger import setup_logger


def main():

    logger = setup_logger()

    logger.info("========== ETL Pipeline Started ==========")

    data = extract_data()

    # Validate the data
    validation_result = validate_data(data)

    # Stop pipeline if validation fails
    if not validation_result:
        logger.error("Validation failed. ETL Pipeline stopped.")
        return

    transformed_data = transform_data(data)

    load_data(transformed_data)

    logger.info("========== ETL Pipeline Completed ==========")


if __name__ == "__main__":
    main()