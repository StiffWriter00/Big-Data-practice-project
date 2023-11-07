""" This is the module responsible for the data manipulation. """

# Import required dependencies
from difflib import get_close_matches
from typing import List
import os
import pandas as pd

# Function to generate the DataFrame comprising all CSV files to work on
def generate_working_data_frame(csv_files: List[str]) -> pd.DataFrame:

    # Check if the CSV file or files were provided
    if not csv_files: raise ValueError("No CSV files provided.")

    # Define a lambda function to check if a file's extension is '.csv'
    is_csv_file: bool = lambda file_path: file_path.lower().endswith('.csv')

    # In case a single CSV file was provided:
    if len(csv_files) == 1:

        # Verify the file's existence and ensure its extension is '.csv'
        file: str = csv_files[0]
        if not os.path.exists(file): raise FileNotFoundError(f"'{file}' does not exist")
        if not is_csv_file(file): raise ValueError(f"'{file}' does not have the .csv extension")

        # If the previous controls were passed, convert the file's content into a DataFrame without duplicate rows and return it
        return _convert_to_data_frame(file).drop_duplicates()

    # In case multiple CSV files were provided:
    else:

        # Initialize an array of DataFrames for the concatenation
        dfs: List[pd.DataFrame] = []

        # Verify the existence of each file and ensure that their extensions are '.csv'
        for file in csv_files:
            if not os.path.exists(file): raise FileNotFoundError(f"'{file}' does not exist")
            if not is_csv_file(file): raise ValueError(f"'{file}' does not have the .csv extension")

            # If the previous controls for a file were passed, convert the file's content into a DataFrame and store it in the array
            dfs.append(_convert_to_data_frame(file))

        # Concatenate all the DataFrames in the array into one comprehensive DataFrame without duplicate rows and return it
        return pd.concat(dfs).drop_duplicates()

# Function to convert a file's content into a DataFrame and ensure its validity
def _convert_to_data_frame(file: str) -> pd.DataFrame:
    try:

        # Create the DataFrame
        df: pd.DataFrame = pd.read_csv(file)

        # Check if the DataFrame's column structure exactly matches the mandatory one
        if tuple(df.columns.tolist()) == ('City','Country','CustomerID','FirstName','LastName','Birthday','Age','Email','Newsletter'):

            # If the column structures match, ensure that the DataFrame's 'Newsletter' column's data will be of type string
            df['Newsletter'] = df['Newsletter'].astype(str) if df['Newsletter'].dtype != str else df['Newsletter']

            # Return the obtained DataFrame
            return df

        # If the columns do not match, raise an error
        else: raise ValueError(f"the columns of {file} are not valid")

    # Error handling
    except ValueError as e:
        raise ValueError(f"Error while reading '{file}': {e}")

# Function to handle numeric outliers in the "Age" column
def handle_age_outliers(df: pd.DataFrame) -> pd.DataFrame:

    # Calculate the first quartile (Q1), third quartile (Q3) and IQR for the 'Age' column
    Q1: float = df['Age'].quantile(0.25)
    Q3: float = df['Age'].quantile(0.75)
    IQR: float = Q3 - Q1

    # Calculate the lower and upper bounds for outliers resolution
    lower_bound: float = Q1 - 1.5 * IQR
    upper_bound: float = Q3 + 1.5 * IQR

    # Identify numeric outliers in the 'Age' column through the use of the calculated bounds
    outliers: List[bool] = (df['Age'] < lower_bound) | (df['Age'] > upper_bound)

    # Assign missing values (NaN) to rows in the 'Age' and 'Birthday' columns where outliers in the 'Age' column are found
    df.loc[outliers, ['Age', 'Birthday']] = pd.NA

    # Impute the missing values in the "Age" column with the column mean
    df["Age"].fillna(df["Age"].mean(), inplace=True)

    # Return the obtained DataFrame
    return df

# Function to correct the spelling mistakes in the "Country" column
def correct_country_spelling(df: pd.DataFrame) -> pd.DataFrame:

    # Initialize a list of correct country names
    correct_countries: List[str] = [
        "United States", "Germany", "Ukraine", "United Kingdom", "Spain", "Poland", "Italy",
        "France", "Netherlands", "Belarus", "Sweden", "Belgium", "Romania", "North Macedonia",
        "Slovakia", "Lithuania", "Bosnia and Herzegovina", "Austria", "Greece", "Ireland",
        "Bulgaria", "Serbia", "Moldova", "Estonia", "Finland", "Latvia", "Croatia", "Hungary",
        "Denmark", "Norway", "Portugal", "Czech Republic"
    ]

    # Apply spelling correction to the "Country" column
    df['Country'] = df['Country'].apply(lambda country: get_close_matches(country, correct_countries, n=1)[0])

    # Return the modified DataFrame
    return df

# Funtion to generate a lookup table that shows the number of occurrences in the "Country" column
def country_lookup_table(df: pd.DataFrame) -> pd.DataFrame:

    # Create the lookup table
    lookup_table = df["Country"].value_counts().reset_index()

    # Rename the lookup table's columns
    lookup_table.columns = ["Country", "Occurrences"]

    # Return the lookup table
    return lookup_table

# Function to store the final DataFrame into an Excel file
def write_to_file(df: pd.DataFrame, output_path: str) -> None:

    # Store the DataFrame into an Excel file
    try:
        df.to_excel(output_path, index=False)
        print(f"The DataFrame was stored into '{output_path}' successfully.")

    # Error handling
    except Exception as e:
        raise Exception(f"Error while writing the output file: {e}")