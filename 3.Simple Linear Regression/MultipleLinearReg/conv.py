import pandas as pd

# Step 1: Extract column names from the .domain file
domain_file = 'cal_housing.domain'  # Replace with your .domain file path

# Read the domain file to get the column names
with open(domain_file, 'r') as file:
    # Extract each line, strip whitespace, and split by ':' to get the feature names
    columns = [line.split(':')[0].strip() for line in file if line.strip()]

# Step 2: Read the .data file using the extracted column names
data_file = 'cal_housing.data'  # Replace with your .data file path
data = pd.read_csv(data_file, header=None, names=columns)

# Step 3: Write the DataFrame to a .csv file
output_csv = 'output_file.csv'  # Replace with your desired output file path
data.to_csv(output_csv, index=False)

print(f'Data successfully converted and saved to {output_csv}')
