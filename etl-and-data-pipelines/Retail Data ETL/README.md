# Retail Data ETL Pipeline

## Project Overview
A Python-based ETL pipeline that extracts retail sales, store and feature datasets from CSV files, transforms the data into fact and dimension datasets using Pandas, and loads the resulting tables into a PostgreSQL database.

The project demonstrates practical data engineering concepts, including data extraction, cleansing, deduplication, date transformations and database integration.

## Technology Stack
- **Python** – ETL development
- **Pandas** – Data manipulation and transformation
- **SQLAlchemy** – Database connectivity
- **PostgreSQL** – Data storage
- **psycopg2** – PostgreSQL database driver

## Project Structure

```text
Retail Data ETL/
│
├── data/
│   ├── Features_dataset.csv
│   ├── sales_dataset.csv
│   └── stores_dataset.csv
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── main.py
├── requirements.txt
└── README.md
```

## ETL Process

### 1. Extract
**Module:** `extract.py`

- Extracts retail sales, store and feature datasets from CSV files.
- Uses Pandas `read_csv()` to load source data into DataFrames.
- Performs initial inspection of sample records and data types.

### 2. Transform
**Module:** `transform.py`

Transforms the extracted datasets into fact and dimension datasets.

| Dataset | Transformation |
|---|---|
| `dim_store` | Removes duplicate store records. |
| `dim_date` | Extracts date, year, month, ISO week and holiday information. |
| `dim_feature` | Removes Markdown columns and duplicate records. |
| `fact_sales` | Creates a copy of the sales dataset. |

Additional transformations:
- Converts date columns into Pandas datetime format.
- Standardises column names to lowercase.
- Resets DataFrame indexes after deduplication.

### 3. Load
**Module:** `load.py`

- Establishes PostgreSQL connectivity using SQLAlchemy.
- Loads the transformed DataFrames into the `retail_db` database.
- Creates or replaces the following tables:

| PostgreSQL Table | Description |
|---|---|
| `fact_sales` | Retail sales transactions |
| `dim_store` | Store attributes |
| `dim_feature` | Store-level feature information |
| `dim_date` | Date and holiday attributes |

Uses Pandas `to_sql()` for database loading.

## Installation & Execution

### 1. Clone the repository

```bash
git clone <repository-url>
cd "Retail Data ETL"
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a PostgreSQL database named `retail_db` and configure the database connection details in the load module.

### 5. Execute the pipeline

```bash
python main.py
```

## Expected Outcome

Successful execution creates four tables in the PostgreSQL database:

- `fact_sales`
- `dim_store`
- `dim_feature`
- `dim_date`

The resulting datasets are available for subsequent SQL analysis, reporting and analytical use cases.

## Key Learning Outcomes

- Building modular Python ETL pipelines.
- Working with multiple CSV source datasets.
- Pandas data cleansing and transformation.
- Creating fact and dimension datasets.
- Date dimension preparation and ISO week extraction.
- PostgreSQL database integration using SQLAlchemy.
- Loading structured datasets into relational databases.

