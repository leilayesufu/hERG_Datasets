import pandas as pd
from rdkit import Chem
from rdkit.Chem import PandasTools

# Load your CSV file
file_path = 'test_dataset.csv'
df = pd.read_csv(file_path)

# Function to calculate InChIKey with error handling
def calculate_inchikey(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        return Chem.inchi.InchiToInchiKey(Chem.MolToInchi(mol)) if mol is not None else None
    except:
        return None

# Add InChIKey column
df['InChIKey'] = df['smiles'].apply(calculate_inchikey)

# Reorder columns
df = df[['smiles', 'InChIKey', 'activity']]

# Save the updated DataFrame to a new CSV file
output_file_path = 'your_updated_file.csv'
df.to_csv(output_file_path, index=False)

print(f"InChIKey column added and saved to {output_file_path}")

