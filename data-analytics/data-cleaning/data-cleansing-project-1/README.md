# Hotel Booking Data Cleansing Project

## 1. Project Overview

This project demonstrates a structured data cleansing and preparation workflow using Python and Pandas on a hotel booking dataset.

The objective is to improve data quality, consistency, and usability by identifying and addressing missing values, correcting data types, standardising column names, handling duplicate records, and creating derived categorical features.

The project follows a practical data preparation approach that can be applied to business reporting, data analytics, and ETL development.

## 2. Business Context

Hotel booking data contains information about reservations, customer characteristics, booking lead times, and reservation outcomes.

Before this data can be reliably used for business analysis or reporting, it needs to be assessed and cleansed to address common data quality issues.

This project focuses on preparing hotel booking records for downstream analytical use by applying data profiling and cleansing techniques.

## 3. Dataset

**Dataset:** Hotel Booking Dataset

**Source:** Local CSV file (`hotel_bookings.csv`)

**Format:** CSV

The dataset contains hotel reservation information, including:

| Data Category | Example Columns |
|---|---|
| Hotel information | `hotel`, `country`, `agent`, `company` |
| Booking information | `lead_time`, `reservation_status_date` |
| Customer information | `adults`, `children`, `babies` |
| Reservation outcome | `is_canceled`, `is_repeated_guest` |

The notebook uses the original hotel booking dataset and performs data cleansing directly on the loaded DataFrame.

## 4. Technologies Used

- Python
- Pandas
- NumPy
- Jupyter Notebook

## 5. Data Cleansing Workflow

### 5.1 Data Loading and Initial Inspection

- Load the CSV dataset into a Pandas DataFrame.
- Inspect the initial records and column names.
- Review DataFrame structure and data types using `info()`.
- Generate descriptive statistics using `describe()`.
- Identify unique values in selected columns to investigate potential anomalies.

### 5.2 Column Standardisation

Rename customer-related columns to improve readability and consistency:

| Original Column | Standardised Column |
|---|---|
| `adults` | `no_of_adults` |
| `children` | `no_of_children` |
| `babies` | `no_of_babies` |

### 5.3 Missing Value Analysis and Treatment

Calculate the percentage of missing values in each column and identify columns requiring cleansing.

| Column | Treatment |
|---|---|
| `agent` | Replace missing values with `-1` to represent the absence of an agent identifier. |
| `no_of_children` | Remove records with missing values after inspecting the affected records. |
| `country` | Replace missing values with `"Unknown"`. |
| `company` | Drop the column because approximately 94% of its values are missing and it provides limited value for the intended analysis. |

Recheck missing values after applying the cleansing rules.

### 5.4 Data Type Standardisation

Convert selected columns to appropriate data types:

- `is_canceled` → Boolean
- `is_repeated_guest` → Boolean
- `no_of_children` → Integer
- `agent` → Integer
- `reservation_status_date` → Datetime

These conversions improve consistency and support downstream analytical operations.

### 5.5 Lead Time Categorisation

Create a new feature, `lead_time_bins`, to categorise booking lead times into groups.

The notebook uses the following intervals:

| Lead Time | Category |
|---|---|
| 0–100 | `0-100` |
| 101–200 | `101-200` |
| 201–300 | `201-300` |
| 301–400 | `301-400` |
| 401–500 | `401-500` |
| 501–600 | `501-600` |
| 601–700 | `601-700` |
| 701–800 | `701-800` |

The categorisation is implemented using `pd.cut()`.

Any missing values in the newly created category column are assigned to the `0-100` category. The new column is positioned next to the original `lead_time` column to improve readability.

### 5.6 String Cleansing

Remove selected special characters (`*`, `-`, and `#`) from the `hotel` column using Pandas regular-expression replacement.

This standardises hotel names for more consistent downstream processing.

### 5.7 Duplicate Record Handling

- Identify duplicate records using `DataFrame.duplicated()`.
- Remove duplicate records while retaining the first occurrence.
- Perform a subsequent duplicate check to validate the cleansing operation.

## 6. Data Quality Techniques Demonstrated

| Technique | Pandas Methods |
|---|---|
| Data inspection | `head()`, `info()`, `describe()` |
| Uniqueness analysis | `nunique()`, `unique()` |
| Missing value profiling | `isna()`, `sum()`, `fillna()` |
| Column transformation | `rename()`, `insert()`, `pop()` |
| Data type conversion | `astype()`, `to_datetime()` |
| Feature engineering | `pd.cut()` |
| String standardisation | `replace()` |
| Duplicate detection | `duplicated()`, `drop_duplicates()` |

## 7. Project Structure

```text
data-cleansing/
│
├── data-cleansing.ipynb
├── data/
│   └── hotel_bookings.csv
└── README.md
```

The CSV file should be stored in the `data/` directory relative to the notebook.

## 8. How to Run the Project

### Prerequisites

Python 3.10 or later, Jupyter Notebook, and the following libraries:

```bash
pip install pandas numpy jupyter
```

### Execution

1. Clone or download the repository.
2. Place `hotel_bookings.csv` inside the `data/` directory.
3. Open the project directory in VS Code or Jupyter Notebook.
4. Update the CSV file path in the notebook to use the project-relative location:

```python
hotel_booking_df = pd.read_csv(
    "data/hotel_bookings.csv"
)
```

5. Run the notebook cells sequentially.

## 9. Expected Outcome

The notebook demonstrates a cleansed and transformed hotel booking DataFrame with:

- Standardised column names.
- Missing values treated according to defined cleansing rules.
- Consistent data types for selected columns.
- Categorised booking lead times.
- Standardised hotel names.
- Duplicate records removed.

The resulting DataFrame can be used as a starting point for further exploratory data analysis, reporting, and analytical processing.

## 10. Key Learning Outcomes

This project demonstrates practical experience in:

- Performing initial data profiling and quality assessment.
- Defining and implementing missing value treatment rules.
- Standardising data structures and data types.
- Applying business-oriented cleansing decisions.
- Creating derived categorical features using Pandas.
- Validating data quality after cleansing operations.

---

**Project Type:** Data Cleansing and Preparation  
**Domain:** Hospitality and Hotel Booking Analytics  
**Primary Skill:** Python Data Analysis with Pandas  
**Portfolio Focus:** Technical Data Business Analysis and Data Quality Management
