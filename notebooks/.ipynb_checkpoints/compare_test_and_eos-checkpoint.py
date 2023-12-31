import pandas as pd

# Read the datasets
combined_dataset = pd.read_csv('combined_dataset_eos.csv')
test_dataset = pd.read_csv('test_dataset.csv')

# Print column names to check for discrepancies
print("Combined Dataset Columns:", combined_dataset.columns)
print("Test Dataset Columns:", test_dataset.columns)

# Identify common molecules based on the "InChiKey" column
common_molecules = set(combined_dataset['InChiKey']).intersection(test_dataset['InChiKey'])

# Remove common molecules from the test dataset
test_dataset_no_common = test_dataset[~test_dataset['InChiKey'].isin(common_molecules)]

# Save the cleaned test dataset to a new CSV file
test_dataset_no_common.to_csv('test_dataset_no_common.csv', index=False)
