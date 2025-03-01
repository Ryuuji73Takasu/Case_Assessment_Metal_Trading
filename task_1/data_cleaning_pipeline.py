import logging
import pandas as pd
import os
import sys

# Configure logging to output to console with a detailed format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize DataFrame column names by stripping whitespace,
    converting to lowercase, and replacing spaces with underscores.
    
    Args:
        df (pd.DataFrame): The DataFrame to standardize.
        
    Returns:
        pd.DataFrame: DataFrame with standardized column names.
    """
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """
    Load an Excel file, standardize column names, fill missing values,
    and convert specified columns to numeric types.
    
    Args:
        file_path (str): Path to the Excel file.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
        
    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        df = pd.read_excel(file_path)
        logging.info(f"Loaded file '{file_path}' with {df.shape[0]} rows and {df.shape[1]} columns.")
    except Exception as e:
        logging.error(f"Error loading file '{file_path}': {e}")
        raise

    df = standardize_columns(df)

    # Define default values for missing data
    fill_values = {
        'quantity': 0,
        'gross_weight': 0,
        'weight': 0,
        # Add more columns with default values if needed
    }
    
    for column, default in fill_values.items():
        if column in df.columns:
            df[column] = df[column].fillna(default)
            logging.info(f"Filled missing values in column '{column}' with default value: {default}")

    # Convert specified columns to numeric types to ensure consistency
    numeric_columns = ['quantity', 'gross_weight', 'weight', 'thickness', 'width']
    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors='coerce')
            logging.info(f"Converted column '{column}' to numeric type.")

    return df

def main():
    # Define input and output file paths
    input_file_1 = "task_1/supplier_data_1.xlsx"
    input_file_2 = "task_1/supplier_data_2.xlsx"
    output_file = "task_1/inventory_dataset.csv"

    try:
        # Load and clean each supplier's dataset
        df1 = load_and_clean_data(input_file_1)
        df2 = load_and_clean_data(input_file_2)
    except FileNotFoundError as e:
        logging.error(e)
        sys.exit(1)
    except Exception as e:
        logging.error(f"An unexpected error occurred during data loading: {e}")
        sys.exit(1)

    try:
        # Merge the cleaned datasets
        inventory_dataset = pd.concat([df1, df2], ignore_index=True)
        logging.info(f"Merged dataset contains {inventory_dataset.shape[0]} rows.")
    except Exception as e:
        logging.error(f"Error merging datasets: {e}")
        sys.exit(1)

    try:
        # Save the cleaned and merged dataset to a CSV file
        inventory_dataset.to_csv(output_file, index=False)
        logging.info(f"Cleaned dataset successfully saved to '{output_file}'.")
    except Exception as e:
        logging.error(f"Error saving cleaned data to CSV: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
