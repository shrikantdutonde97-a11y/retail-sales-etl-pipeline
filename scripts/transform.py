import pandas as pd

def transform_data(dataframes):
    """
    Apply transformations to each DataFrame.
    """

    for filename, df in dataframes.items():

        # Convert Date column to datetime
        df["Date"] = pd.to_datetime(df["Date"])

        print(f"\nTransformation completed for: {filename}")

    return dataframes


from ingest import extract_data

if __name__ == "__main__":
    data = extract_data()

    transformed_data = transform_data(data)

    for filename, df in transformed_data.items():
        print("\nData Types:")
        print(df.dtypes)    