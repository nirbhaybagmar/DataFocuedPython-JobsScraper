import pandas as pd
import numpy as np

def clean_and_aggregate_data(input_csv, output_csv):
    """
    Cleans and aggregates the data from a specified CSV file.

    Args:
        input_csv (str): Path to the input CSV file containing the data to be cleaned.
        output_csv (str): Path to save the cleaned and aggregated data as a CSV file.
    """

    # Reading data from the CSV file
    final_data = pd.read_csv(input_csv)

    # Filling missing values in 'Job-Type' with 'Not Applicable'
    final_data['Job-Type'] = final_data['Job-Type'].fillna('Not Applicable')

    # Filling missing values in 'Location', 'Salary', and 'Tech' columns
    columns_to_fill = ['Location', 'Salary', 'Tech']
    final_data[columns_to_fill] = final_data[columns_to_fill].fillna('Not Applicable')

    # Removing rows where 'Company' is NaN
    final_data = final_data[final_data['Company'].notna()]

    # Saving the cleaned and aggregated data to a CSV file
    final_data.to_csv(output_csv, index=False)


if __name__ == '__main__':
    input_csv_path = 'glassdoor/jobs.csv'
    output_csv_path = 'data_aggregation.csv'
    clean_and_aggregate_data(input_csv_path, output_csv_path)
