import pandas as pd
from rdkit import Chem
from rdkit.Chem import inchi

# Load the CSV file
df = pd.read_csv('eos2ta5.csv')

# Check if 'smiles' column exists (case-insensitive)
smiles_column = 'smiles'
if smiles_column.lower() not in map(str.lower, df.columns):
    raise ValueError(f"The '{smiles_column}' column is not present in the CSV file.")

# Define a function to convert SMILES to InChIKey
def smiles_to_inchikey(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        inchi_key = inchi.MolToInchiKey(mol)
        return inchi_key
    except Exception as e:
        return f"Error: {e}"

# Create a new column for InChIKey
df['InChIKey'] = df['smiles'].apply(smiles_to_inchikey)

# Save the updated DataFrame to a new CSV file
df.to_csv('output_file.csv', index=False)

