#!/usr/bin/env python

"""
This is the main module, where the entire process takes place.
In here you can have a general overview of the steps taken to get the end result.
"""

# Import required dependencies
from typing import List
import os
import sys

# Main function
def main(csv_files: List[str]) -> None:
    from src import data

    # Step 1 --> Generate the working DataFrame
    print("Generating the working DataFrame...")
    working_df = data.generate_working_data_frame(csv_files)

    # Step 2 --> Handle the outliers in the "Age" column
    print("Handling the outliers in the 'Age' column...")
    working_df = data.handle_age_outliers(working_df)

    # Step 3 --> Correct spelling mistakes in the "Country" column
    print("Correcting spelling mistakes in the 'Country' column...")
    working_df = data.correct_country_spelling(working_df)

    # Step 4 --> Generate a lookup table to show the occurrencies in the "Country" column
    print(f"\nShowing the country occurrences lookup table:\n{data.country_lookup_table(working_df)}\n")

    # Final step --> Store the final DataFrame into an Excel file
    print("Storing the final DataFrame into a file...")
    data.write_to_file(working_df, os.path.join(path, 'output.xlsx'))

# Check if this module is executed as the main program
if __name__ == '__main__':

    # Obtain the script's absolute path
    path: str = os.path.dirname(__file__)
    if path.endswith('/.'): path = path[:-2]

    # Dynamic runtime parameters handling
    main([os.path.join(path, 'data', 'CustomerInfoSystem1.csv'), os.path.join(path, 'data', 'CustomerInfoSystem2.csv')]) if len(sys.argv) < 2 else main(sys.argv[1:])

# If this module is not executed as the main program, raise an error
else:
    raise RuntimeError("This module should only be run as the main program rather than being imported")