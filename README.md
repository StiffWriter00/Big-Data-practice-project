# Big Data practice project

## A Python project for practicing Big Data analysis.
It was developed with the following versions of Python and PIP:
- **Python --> 3.11.5**
- **PIP --> 23.2.1**

## Setup instructions
To run the script, you need to set up the virtual environment by following these steps:

1. Install Python and PIP.
2. Clone the repository.
3. Open a terminal and go to the project directory.
4. Create the virtual environment by running:
    - `python3 -m venv venv`
5. Activate the virutal environment by running:
    - **FOR WINDOWS:** `venv\Scripts\activate`
    - **FOR MAC/LINUX:** `source venv/bin/activate`
6. Install the necessary dependencies by running:
    - `pip install -r requirements.txt`
- **OPTIONAL** You may be asked to upgrade PIP in the virtual environment.<br>
  It's not mandatory, but you can do so if you want by following the instructions in the prompt.
- **EXTRA** Once you are done using the script, you can deactivate the virtual environment by running:
    - `deactivate`

## Running the script
After creating the virtual environment, there are two ways to run the script:

- Run the script directly using the CSV files in the `data` folder (for demonstration):
    - **FOR WINDOWS:** `python.exe main.py`
    - **FOR MAC/LINUX:** `python3 main.py`
- Run the script with custom runtime parameters (using other CSV files):
    - **FOR WINDOWS (e.g.):** `python.exe main.py path_to_csv_file_1.csv path_to_csv_file_2.csv`
    - **FOR MAC/LINUX (e.g.):** `python3 main.py path_to_csv_file_1.csv path_to_csv_file_2.csv`

## CSV File Format
The script requires CSV files with the following columns:

| City | Country | CustomerID | FirstName | LastName  | Birthday   | Age | Email | Newsletter |
| ---- | ------- | ---------- | --------- | --------- | ---------- | --- | ----- | ---------- |
| ...  | ...     | ...        | ...       | ...       | ...        | ... | ...   | ...        |

Please ensure that your CSV files contain data in this format for the script to work correctly.