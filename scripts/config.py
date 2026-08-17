from pathlib import Path


# Project root folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data folders
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

# Expected columns in the retail sales dataset
EXPECTED_COLUMNS = [
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