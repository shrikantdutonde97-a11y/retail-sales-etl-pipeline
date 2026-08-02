from ingest import extract_data
from validate import validate_data
from transform import transform_data
from load import load_data


def main():

    print("========== ETL Pipeline Started ==========")

    data = extract_data()

    validate_data(data)

    transformed_data = transform_data(data)

    load_data(transformed_data)

    print("\n========== ETL Pipeline Completed ==========")


if __name__ == "__main__":
    main()