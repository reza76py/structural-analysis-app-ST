# data_input/nodes_data.py

import pandas as pd
import numpy as np

def read_nodes_from_excel(file_path="data_input/nodes.xlsx"):
    """
    Reads node coordinates (X, Y, Z) from an Excel file and returns them as a NumPy array.
    The Excel file must have columns named 'x', 'y', 'z' (case-insensitive).
    """
    df = pd.read_excel(file_path)

    # Normalize column names
    df.columns = df.columns.str.lower()

    # Drop rows with missing values
    df = df.dropna(subset=['x', 'y', 'z'])

    # Extract and return coordinates
    nodes = df[['x', 'y', 'z']].values
    return nodes
