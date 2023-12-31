import pandas as pd
import os
from rdkit import Chem

# Replace 'dataset1.csv', 'dataset2.csv', etc., with your actual dataset filenames
datasets = ['output.csv', 'output2.csv']

# Load and process each dataset
dfs = []
for dataset in datasets:
    df = pd.read_csv(dataset)
    
    # Remove rows with missing or invalid SMILES
    df = df.dropna(subset=['smiles'])
    df['smiles'] = df['smiles'].astype(str)
    df = df[df['smiles'].apply(lambda x: Chem.MolFromSmiles(x) is not None)]
    
    # Remove duplicates based on SMILES
    df = df.drop_duplicates(subset=['smiles'])
    
    # Add the processed DataFrame to the list
    dfs.append(df)

# Concatenate all DataFrames
result_df = pd.concat(dfs, ignore_index=True)

# Save the combined and processed DataFrame to a new CSV file
result_df.to_csv('test_dataset.csv', index=False)
