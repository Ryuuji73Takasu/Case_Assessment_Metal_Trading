# Vanilla Steel Data Analyst Case Assessment

This repository contains my solution for the Vanilla Steel case assessment. The solution includes:

- **Data Cleaning & Preparation:** Python scripts to ingest, clean, and merge supplier data.
- **Analysis & Insights:** SQL queries for generating dashboards on account manager performance and revenue reporting.
- **Buyer Preference Matching:** A Python pipeline to match supplier data with buyer preferences, outputting a final recommendations table.

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Looker Studio Report](#looker-studio-report)
- [Documentation](#documentation)
- [Contact](#contact)

## Project Overview

The objective of this assessment is to design and implement data pipelines that:
- Clean and merge supplier datasets.
- Generate analytical dashboards for the sales team.
- Create a recommendation system that matches supplier materials to buyer preferences.

I utilized Python for data cleaning, SQL for querying, and Google BigQuery for scalable data storage and processing. The dashboards are built with Looker Studio.

## Repository Structure

    ```bash
    Case_Assessment_Metal_Trading/
    ├── README.md                      # Project overview and instructions
    ├── .gitignore                     # Files and folders to ignore
    ├── requirements.txt               # Python dependencies list
    ├── task_1/                        # Data cleaning & preparation
    │   ├── supplier_data_1.xlsx       # Raw supplier data file
    │   ├── supplier_data_2.xlsx       # Raw supplier data file
    │   └── data_cleaning_pipeline.py  # Python script for cleaning & merging data
    │   └── inventory_dataset.csv      # CSV file generated with inventory data
    ├── task_2/                        # Analysis & insights (dashboards)
    │   ├── deals.csv                  # Deals data for dashboards
    │   ├── account_manager_dashboard.sql   # SQL query for account manager performance
    │   └── revenue_reporting_dashboard.sql # SQL query for revenue reporting
    ├── task_3/                        # Buyer preference matching
    │   ├── supplier_data_1.xlsx       # Supplier data file for recommendation matching
    │   ├── supplier_data_2.xlsx       # Supplier data file for recommendation matching
    │   ├── buyer_preferences.xlsx     # Buyer preferences file
    │   └── recommendation_pipeline.py # Python script for matching logic
    └── docs/                          # Documentation and process notes
    │    └── process_documentation.md   # Detailed explanation of the project
    


# Detailed explanation of the project

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your_username/VanillaSteel_Case_Assessment.git
   cd VanillaSteel_Case_Assessment

2. **Install Dependencies:**
    ```
    pip install -r requirements.txt



## Usage


**Task 1: Data Cleaning & Preparation**

Run the data cleaning script:

    python task_1/data_cleaning_pipeline.py

This script will read the supplier Excel files, clean the data, merge the datasets, and output a cleaned CSV file.

**Task 2: Analysis & Insights**

*SQL Queries:*

Use the provided SQL queries in task_2/ to analyze the deals data. These queries are designed to be executed on your Google BigQuery dataset.

    account_manager_dashboard.sql
    revenue_reporting_dashboard.sql

*Looker Studio:*

Looker Studio has the created dashboards based on these queries.


## Looker Studio Report

Access the Looker Studio dashboards using the following link: [Looker Studio Report](https://lookerstudio.google.com/reporting/ce6e43c2-e790-4ea9-a8b4-0c51453b9828)


## Documentation


Refer to

    docs/process_documentation.md
for a detailed description of the tools, processes, and decisions taken during the project.

## Contact


For any questions, please [contact me](mailto:sourav.raihan31@gmail.com).