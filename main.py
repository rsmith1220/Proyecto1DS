import os
import pandas as pd

def combine_csv_files(input_folder):
    all_dataframes = []

    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            filepath = os.path.join(input_folder, filename)
            # Read CSV file into a Pandas DataFrame
            df = pd.read_csv(filepath)
            all_dataframes.append(df)

    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(all_dataframes, ignore_index=True)

    # Save the combined DataFrame to a CSV file
    combined_df.to_csv('combinado.csv', index=False)

if __name__ == "__main__":
    input_folder = "Data"  # Replace with the actual path of your folder containing .csv files
    combine_csv_files(input_folder)
