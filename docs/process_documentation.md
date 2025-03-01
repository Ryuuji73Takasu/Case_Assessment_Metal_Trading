# Process Documentation

This document explains the tools, processes, and rationale behind each task in the Vanilla Steel Data Analyst Case Assessment. It covers how I cleaned up supplier data, generate analytical dashboards, and created a recommendation system to match buyer preferences with supplier materials.

---

## Table of Contents

1. [Overview of Tasks](#overview-of-tasks)  
2. [Tools and Dependencies](#tools-and-dependencies)  
3. [Task 1: Data Cleaning & Preparation](#task-1-data-cleaning--preparation)  
4. [Task 2: Analysis & Insights](#task-2-analysis--insights)  
5. [Task 3: Buyer Preference Matching](#task-3-buyer-preference-matching)  
6. [Conclusion & Recommendations](#conclusion--recommendations)

---

## Overview of Tasks

1. **Task 1: Data Cleaning & Preparation**  
   - Ingest and merge raw supplier data.  
   - Clean/standardize columns and handle missing values.  
   - Output a unified, cleaned CSV file.

2. **Task 2: Analysis & Insights**  
   - Use SQL queries to generate insights on account manager performance and revenue reporting.  
   - Build dashboards in Looker Studio for visualization.

3. **Task 3: Buyer Preference Matching**  
   - Match supplier materials with buyer preferences based on grade, finish, thickness, etc.  
   - Filter results by max weight, min quantity if needed.  
   - Produce a final `recommendations.csv` with matched rows.

---

## Tools and Dependencies

Python, SQL, BigQuery and Looker Studio were used
Python dependencies are in the `requirements.txt`

- **pandas**  
  Used for reading Excel/CSV files, cleaning data, merging DataFrames, and performing transformations.

- **openpyxl**  
  A helper library required by pandas to read and write `.xlsx` files.

---

## Task 1: Data Cleaning & Preparation

### Goal
- **Combine** raw supplier data from multiple Excel files.
- **Clean** them by standardizing columns, handling missing values.
- **Output** a single CSV for further analysis.

### Process
1. **Read Excel Files**  
   - Use `pandas.read_excel()` for each supplier file.  
2. **Concatenate**  
   - Use `pd.concat()` to unify data into one DataFrame.  
3. **Clean & Standardize**  
   - Converted column names to lowercase for better handling.
   - Converted numeric fields (e.g., thickness, weight) to floats.  
4. **Handle Missing Data**  
   - Used (`dropna`) rows as needed.  
5. **Output**  
   - Save a cleaned CSV (e.g., `inventory_dataset.csv`).

### Tools
- **pandas** + **openpyxl** for reading Excel and cleaning.

---

## Task 2: Analysis & Insights

### Goal
- Generate **analytical dashboards** for:
  - **Account Manager Performance**  
  - **Revenue Reporting**  

### Process
1. **Deals Data**  
   - CSV (`deals.csv`) loaded into BigQuery.  
2. **SQL Queries**  
   - `account_manager_dashboard.sql` for manager performance logic.  
   - `revenue_reporting_dashboard.sql` for buyer-side revenue analysis.  
3. **Looker Studio**  
   - Connected to BigQuery Sandbox version.  
   - Built dashboards with scorecard and bar chart.

### Tools
- **SQL** for transformations and aggregations.  
- **Looker Studio** for visualization.  
- **BigQuery** if storing data in the cloud. I saved two views for using as a data source.

---

## Task 3: Buyer Preference Matching

### Goal
- **Match** supplier materials to buyer preferences:
  - `grade == preferred_grade`
  - `finish == preferred_finish`
  - `thickness == preferred_thickness`
  - `(optional) width == preferred_width`
- **Filter** by weight <= max_weight and quantity >= min_quantity if those fields exist.
- **Output** `recommendations.csv`.

### Process
1. **Combine** supplier data from two Excel files.  
2. **Standardize** columns (e.g., `"thickness_(mm)"` → `"thickness"`).  
3. **Join** with buyer data on `(grade, finish, thickness, width)`.  
4. **Filter** by `weight <= max_weight` and `quantity >= min_quantity` if needed.  
5. **Save** final matches to `recommendations.csv`.

### Tools
- **pandas** for merging, filtering, and writing the final CSV.
- **openpyxl** for Excel reading.

---

## Conclusion & Recommendations

- **Data Cleaning** (Task 1) ensures supplier data is consistent for further analysis.  
- **Analysis & Insights** (Task 2) uses SQL + Looker Studio to provide interactive dashboards.  
- **Buyer Preference Matching** (Task 3) merges supplier data with buyer preferences, producing a final `recommendations.csv` for each buyer’s matched materials.

### Recommendations

Please provide feedback for better suggestions on how to improve this case assessment. Thank you!

**End of Document**


