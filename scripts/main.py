from ingest import extract_data
from validate import validate_data
from transform import transform_data
from load import load_data
from logger import setup_logger


def main():

    logger = setup_logger()

    logger.info("========== ETL Pipeline Started ==========")

    data = extract_data()

    validate_data(data)

    transformed_data = transform_data(data)

    load_data(transformed_data)

    logger.info("========== ETL Pipeline Completed ==========")


if __name__ == "__main__":
    main()