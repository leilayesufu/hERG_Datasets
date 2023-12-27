import pandas as pd
from rdkit import Chem
from rdkit.Chem import inchi

# Load the CSV file
df = pd.read_csv('eos2ta5.csv')

# Define a function to convert SMILES to InChIKey
def smiles_to_inchikey(smiles):
    mol = Chem.MolFromSmiles(smiles)
    inchi_key = inchi.MolToInchiKey(mol)
    return inchi_key

# Create a new column for InChIKey
df['InChIKey'] = df['SMILES'].apply(smiles_to_inchikey)

# Save the updated DataFrame to a new CSV file
df.to_csv('output_file.csv', index=False)

