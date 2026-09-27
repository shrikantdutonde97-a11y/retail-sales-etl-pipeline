# Retail Sales ETL Pipeline

A modular **Python-based ETL (Extract, Transform, Load) pipeline** for processing and validating retail sales data. The project reads raw CSV files, performs data-quality checks and transformations, and generates a cleaned processed dataset for downstream analytics.

---

## 📌 Project Overview

The **Retail Sales ETL Pipeline** is designed to automate the preparation of retail sales data for analysis.

The pipeline follows a modular ETL architecture:

**Raw CSV Data → Extract → Validate → Transform → Load → Processed CSV**

The project focuses on building a reliable and reusable data engineering workflow using **Python, Pandas, logging, data validation, and Git/GitHub**.

---

## 🎯 Project Objectives

* Automate the extraction of retail sales data from CSV files.
* Validate the incoming data before processing.
* Detect missing values, duplicate records, and invalid columns.
* Transform and clean the dataset.
* Validate sales amount calculations.
* Generate a processed dataset for analytics.
* Maintain logs for pipeline execution and troubleshooting.
* Organize the project using a modular ETL structure.
* Track project development using Git and GitHub.

---

## 🏗️ ETL Architecture

```text
                 ┌─────────────────────┐
                 │   Raw CSV Files     │
                 │    data/raw/        │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      Extract        │
                 │     ingest.py       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │      Validate       │
                 │     validate.py     │
                 └──────────┬──────────┘
                            │
                       Validation
                         Passed
                            │
                            ▼
                 ┌─────────────────────┐
                 │     Transform       │
                 │    transform.py     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │        Load         │
                 │       load.py       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Processed CSV Data  │
                 │  data/processed/    │
                 └─────────────────────┘
```

---

## 🛠️ Technologies Used

| Technology     | Purpose                                |
| -------------- | -------------------------------------- |
| Python         | ETL pipeline development               |
| Pandas         | Data processing and transformation     |
| NumPy          | Data manipulation support              |
| Python Logging | Pipeline monitoring and execution logs |
| Git            | Version control                        |
| GitHub         | Source code repository                 |

---

## 📂 Project Structure

```text
Retail_Sales_ETL_Pipeline/
│
├── data/
│   ├── raw/
│   │   └── retail_sales_dataset.csv
│   │
│   └── processed/
│       └── retail_sales_dataset_processed.csv
│
├── scripts/
│   ├── ingest.py
│   ├── ingest_v1.py
│   ├── validate.py
│   ├── transform.py
│   ├── load.py
│   ├── logger.py
│   └── main.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── pipeline.log
```

---

# 🔄 ETL Pipeline

## 1. Extract

The extraction module reads CSV files from the `data/raw/` directory.

### File

```text
scripts/ingest.py
```

The pipeline automatically identifies CSV files in the raw data directory and loads them using Pandas.

Example:

```python
df = pd.read_csv(file_path)
```

The extracted data is then passed to the validation stage.

---

## 2. Validate

Before transforming the data, the pipeline performs data-quality checks.

### File

```text
scripts/validate.py
```

The validation process checks:

* Expected columns
* Missing columns
* Unexpected/extra columns
* Null values
* Duplicate records

The expected dataset columns are:

```text
Transaction ID
Date
Customer ID
Gender
Age
Product Category
Quantity
Price per Unit
Total Amount
```

If validation fails, the pipeline stops instead of processing potentially incorrect data.

Example validation result:

```text
Validation PASSED
```

---

## 3. Transform

After successful validation, the data is transformed and cleaned.

### File

```text
scripts/transform.py
```

Current transformations include:

### Date Conversion

The `Date` column is converted into a proper datetime format.

```python
df["Date"] = pd.to_datetime(df["Date"])
```

### Total Amount Validation

The pipeline verifies that:

```text
Total Amount = Quantity × Price per Unit
```

Example:

```python
df["Quantity"] * df["Price per Unit"]
```

The pipeline checks the calculated value against the existing `Total Amount` column.

Example result:

```text
Total Amount check PASSED
```

---

## 4. Load

The transformed dataset is written to the processed data directory.

### File

```text
scripts/load.py
```

Output location:

```text
data/processed/
```

The processed CSV can then be used for further analytics and visualization.

---

# 📊 Dataset

The project currently uses a retail sales dataset containing **1,000 records and 9 columns**.

### Dataset Columns

| Column           | Description                   |
| ---------------- | ----------------------------- |
| Transaction ID   | Unique transaction identifier |
| Date             | Date of the transaction       |
| Customer ID      | Customer identifier           |
| Gender           | Customer gender               |
| Age              | Customer age                  |
| Product Category | Product category purchased    |
| Quantity         | Number of units purchased     |
| Price per Unit   | Price of one unit             |
| Total Amount     | Total transaction amount      |

---

# 🔍 Data Quality Checks

The pipeline performs several data-quality checks before transformation.

### Missing Values

The pipeline checks every column for null/missing values.

### Duplicate Records

Duplicate rows are detected before processing.

For example, if duplicate records are introduced into the raw dataset, validation fails and prevents the pipeline from continuing.

### Schema Validation

The pipeline checks whether the incoming dataset contains the expected columns.

### Business Rule Validation

The pipeline verifies the relationship:

```text
Total Amount = Quantity × Price per Unit
```

This helps identify inconsistent sales values.

---

# 📝 Logging

The project uses Python's logging functionality to record pipeline execution.

### File

```text
pipeline.log
```

The logs provide information about:

* Pipeline start
* File extraction
* Number of records loaded
* Validation results
* Transformation results
* Output file creation
* Pipeline completion
* Errors encountered during execution

Example:

```text
ETL Pipeline Started
Loaded 1000 rows / 9 columns
Validation PASSED
Total Amount check PASSED
Transformation completed
Saved 1000 rows to processed CSV
ETL Pipeline Completed
```

---

# ▶️ How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/shrikantdutonde97-a11y/retail-sales-etl-pipeline.git
```

Navigate into the project:

```bash
cd retail-sales-etl-pipeline
```

---

## 2. Create a Virtual Environment

On Windows:

```powershell
python -m venv venv
```

Activate the environment:

```powershell
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the ETL Pipeline

Run the main pipeline:

```bash
python scripts/main.py
```

The pipeline executes the following sequence:

```text
Extract
   ↓
Validate
   ↓
Transform
   ↓
Load
```

---

## 5. Check the Output

After successful execution, the processed dataset will be available in:

```text
data/processed/
```

The pipeline log will be available in:

```text
pipeline.log
```

---

# 🧩 Modular Design

The pipeline is divided into separate modules so that each ETL stage can be developed, tested, and maintained independently.

| File           | Responsibility                     |
| -------------- | ---------------------------------- |
| `main.py`      | Controls the complete ETL workflow |
| `ingest.py`    | Extracts raw CSV data              |
| `validate.py`  | Performs data-quality validation   |
| `transform.py` | Cleans and transforms data         |
| `load.py`      | Saves processed data               |
| `logger.py`    | Configures pipeline logging        |

This modular approach makes the pipeline easier to maintain and extend.

---

# 🔄 Pipeline Workflow

The main pipeline is controlled through:

```text
scripts/main.py
```

The workflow is:

```text
Start
  │
  ▼
Extract Data
  │
  ▼
Validate Data
  │
  ├── Failed → Stop Pipeline
  │
  ▼
Transform Data
  │
  ▼
Load Processed Data
  │
  ▼
Pipeline Completed
```

---

# 🧪 Error Handling and Validation

The pipeline is designed to stop processing when important data-quality problems are detected.

For example:

```text
Raw Data
   ↓
Validation
   ↓
Duplicate Records Found
   ↓
Validation FAILED
   ↓
Pipeline Stops
```

This prevents invalid data from being passed to downstream processing.

---

# 📈 Future Enhancements

The project is planned to be extended into a cloud-based data engineering and analytics platform.

Planned enhancements include:

### ☁️ AWS S3

* Store raw data in Amazon S3.
* Organize data into raw and processed zones.
* Automate data uploads.
* Use cloud storage as the central data lake layer.

### ⚡ Apache Spark

* Process larger datasets using Spark.
* Explore distributed data processing.
* Integrate Spark into the ETL workflow where appropriate.

### ❄️ Snowflake

* Build a cloud data warehouse.
* Load processed retail data into Snowflake.
* Create analytical tables.
* Perform SQL-based analysis.

### 📊 Power BI

* Connect Power BI to the analytical data.
* Build an interactive retail sales dashboard.
* Create KPIs and visualizations.
* Analyze sales by product category, customer, gender, and time.

### 🔄 Cloud-Based Architecture

The planned architecture is:

```text
Retail CSV Data
      │
      ▼
Python ETL
      │
      ▼
   AWS S3
      │
      ▼
  Snowflake
      │
      ▼
   Power BI
      │
      ▼
Analytics Dashboard
```

---

# 🎓 Learning Outcomes

Through this project, the following concepts are being practiced:

* ETL pipeline development
* Data extraction
* Data cleaning
* Data validation
* Data transformation
* Data-quality checks
* Python and Pandas
* Modular programming
* Logging
* Error handling
* Git and GitHub
* Data engineering workflow
* Cloud data engineering concepts

---

# 🚀 Project Status

### Current Status

* [x] Dataset collected
* [x] Project structure created
* [x] Python environment configured
* [x] CSV extraction implemented
* [x] Data validation implemented
* [x] Data transformation implemented
* [x] Data-quality checks implemented
* [x] Processed dataset generated
* [x] Logging implemented
* [x] Git repository initialized
* [x] Project pushed to GitHub
* [x] Version history maintained

### Planned

* [ ] AWS S3 integration
* [ ] Cloud-based data storage
* [ ] Apache Spark integration
* [ ] Snowflake data warehouse
* [ ] Power BI dashboard
* [ ] End-to-end cloud ETL pipeline

---

# 👨‍💻 Author

**Shrikant Dutonde**

Final-year Computer Engineering Student

Interested in:

* Data Engineering
* Cloud Computing
* Python
* SQL
* Big Data
* AWS
* Data Analytics

---

# 📌 Repository

GitHub Repository:

```text
https://github.com/shrikantdutonde97-a11y/retail-sales-etl-pipeline
```

---

## ⭐ Future Vision

The goal of this project is to evolve the current Python-based ETL pipeline into a complete **cloud-based retail data engineering and analytics platform**, combining:

**Python + AWS S3 + Apache Spark + Snowflake + Power BI**

The final system will provide an end-to-end workflow for collecting, processing, storing, analyzing, and visualizing retail sales data.
