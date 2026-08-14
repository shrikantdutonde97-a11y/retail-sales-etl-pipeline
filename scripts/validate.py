from logger import setup_logger
from ingest import extract_data


def validate_data(dataframes):
    """
    Validate each DataFrame in the dictionary.
    Returns True if all files pass validation,
    otherwise returns False.
    """

    logger = setup_logger()

    # IMPORTANT: This must be BEFORE the for loop
    validation_passed = True

    for filename, df in dataframes.items():

        logger.info("=" * 50)
        logger.info(f"Validating: {filename}")
        logger.info("=" * 50)

        try:
            logger.info(f"Column Names: {df.columns.tolist()}")

            logger.info(f"\nData Types:\n{df.dtypes}")

            logger.info(f"\nMissing Values:\n{df.isnull().sum()}")

            logger.info(f"Duplicate Rows: {df.duplicated().sum()}")

            # Calculate total problems
            missing_values = df.isnull().sum().sum()
            duplicate_rows = df.duplicated().sum()

            # Check validation
            if missing_values == 0 and duplicate_rows == 0:

                logger.info(f"Validation PASSED for {filename}")

            else:

                logger.warning(
                    f"Validation FAILED for {filename} - "
                    f"Missing values: {missing_values}, "
                    f"Duplicate rows: {duplicate_rows}"
                )

                validation_passed = False

        except Exception as e:

            logger.error(f"Validation failed for {filename}: {e}")

            validation_passed = False

    # IMPORTANT: This must be AFTER the for loop
    return validation_passed


if __name__ == "__main__":

    data = extract_data()

    result = validate_data(data)

    print(f"Validation Result: {result}")