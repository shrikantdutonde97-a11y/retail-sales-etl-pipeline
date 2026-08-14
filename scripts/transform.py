from logger import setup_logger
import pandas as pd

def transform_data(dataframes):
    """
    Apply transformations to each DataFrame.
    """
    logger = setup_logger()

    for filename, df in dataframes.items():

        logger.info(f"Starting transformation for: {filename}")

        try:
            # Convert Date column to datetime
            df["Date"] = pd.to_datetime(df["Date"])

                        # Check Total Amount calculation
            calculated_amount = (
                df["Quantity"] * df["Price per Unit"]
            )

            invalid_amounts = (
                df["Total Amount"] != calculated_amount
            ).sum()

            if invalid_amounts == 0:
                logger.info(
                    f"Total Amount check PASSED for {filename}"
                )
            else:
                logger.warning(
                    f"Total Amount check FAILED for {filename}: "
                    f"{invalid_amounts} incorrect records"
                )

            logger.info(
                f"Transformation completed for: {filename}"
            )

        except Exception as e:
            logger.error(
                f"Transformation failed for {filename}: {e}"
            )
    return dataframes


from ingest import extract_data

if __name__ == "__main__":
    data = extract_data()

    transformed_data = transform_data(data)

    for filename, df in transformed_data.items():
        print("\nData Types:")
        print(df.dtypes)    