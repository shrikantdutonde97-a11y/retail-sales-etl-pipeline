def validate_data(dataframes):
    """
    Validate each DataFrame in the dictionary.
    """

    for filename, df in dataframes.items():

        print(f"\n{'='*50}")
        print(f"Validating: {filename}")
        print(f"{'='*50}")

        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

from ingest import extract_data

if __name__ == "__main__":
    data = extract_data()
    validate_data(data)