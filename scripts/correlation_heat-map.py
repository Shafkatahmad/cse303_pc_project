import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load dataset
df = pd.read_csv("data/raw/laptop_price.csv")

# Select only numeric columns  
numeric_df = df.select_dtypes(include=[np.number])

# Calculate the correlation matrix  
correlation_matrix = numeric_df.corr()

# Plot the heatmap using Matplotlib
plt.figure(figsize=(10, 8))
cax = plt.matshow(correlation_matrix, cmap='coolwarm')

# Add a color bar for reference
plt.colorbar(cax)

# Add column and row labels
plt.xticks(np.arange(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(np.arange(len(correlation_matrix.columns)), correlation_matrix.columns)

# Title and layout adjustments
plt.title('Correlation Heatmap of Laptop Price Dataset')
plt.tight_layout()
output_dir = "./outputs/figures"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'correlation_heat-map.png'))

# Show the plot
plt.show()
