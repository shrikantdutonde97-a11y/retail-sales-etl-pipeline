from logger import setup_logger
from ingest import extract_data


def validate_data(dataframes):
    """
    Validate each DataFrame in the dictionary.
    Returns True if all files pass validation,
    otherwise returns False.
    """

    logger = setup_logger() 

    expected_columns = [
    "Transaction ID",
    "Date",
    "Customer ID",
    "Gender",
    "Age",
    "Product Category",
    "Quantity",
    "Price per Unit",
    "Total Amount"
]
    expected_dtypes = {
    "Transaction ID": "int64",
    "Customer ID": "object",
    "Gender": "object",
    "Age": "int64",
    "Product Category": "object",
    "Quantity": "int64",
    "Price per Unit": "int64",
    "Total Amount": "int64"
}

    # IMPORTANT: This must be BEFORE the for loop
    validation_passed = True

    for filename, df in dataframes.items():

        logger.info("=" * 50)
        logger.info(f"Validating: {filename}")
        logger.info("=" * 50)

        try:
            logger.info(f"Column Names: {df.columns.tolist()}") 

            missing_columns = set(expected_columns) - set(df.columns)
            extra_columns = set(df.columns) - set(expected_columns)

            if missing_columns:
                logger.warning(
                f"Missing columns in {filename}: {missing_columns}"
                )
                validation_passed = False

            if extra_columns:
                logger.warning(
                f"Unexpected columns in {filename}: {extra_columns}"
                )
                validation_passed = False

            if not missing_columns and not extra_columns:
                logger.info(f"Schema check PASSED for {filename}")

            logger.info(f"\nData Types:\n{df.dtypes}")

            # Data type validation
            for column, expected_type in expected_dtypes.items():

                if column in df.columns:

                    actual_type = str(df[column].dtype)

                    if actual_type == expected_type:
                        logger.info(
                            f"Data type check PASSED: {column} -> {actual_type}"
                        )
                    else:
                        logger.warning(
                            f"Data type check FAILED: {column} -> "
                            f"Expected: {expected_type}, "
                            f"Found: {actual_type}"
                        )

                        validation_passed = False

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