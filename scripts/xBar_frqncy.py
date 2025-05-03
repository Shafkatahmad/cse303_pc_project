import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("data/raw/laptop_price.csv")

# Iterate through each column
for column in df.columns:
    print(f"\n--- Analyzing Column: {column} ---")  
    if pd.api.types.is_numeric_dtype(df[column]):
        # Drop NaNs for numerical calculations
        col_data = df[column].dropna()
        mean = col_data.mean()
        median = col_data.median()
        variance = col_data.var()
        std_dev = col_data.std()  
        print(f"Type: Numerical")
        print(f"Mean: {mean}")
        print(f"Median: {median}")
        print(f"Variance: {variance}")
        print(f"Standard Deviation: {std_dev}")
    else:
        # For categorical or non-numeric
        print(f"Type: Categorical / Discrete")
        freq = df[column].value_counts()
        percent = df[column].value_counts(normalize=True) * 100
        summary = pd.DataFrame({'Frequency': freq, 'Percentage (%)': percent.round(2)})
        print(summary)
