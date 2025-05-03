import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("data/raw/laptop_price.csv")

# Create price-based categories
df['Price_Class'] = pd.cut(df['Price (Euro)'],
                           bins=[0, 700, 1200, df['Price (Euro)'].max()],
                           labels=['Budget', 'Midrange', 'Premium'])

# Count the samples in each category
class_counts = df['Price_Class'].value_counts() 
print(class_counts)

# Visualize the distribution
class_counts.plot(kind='bar', title='Price Category Distribution')
plt.xlabel('Price Class')
plt.ylabel('Number of Laptops')

# Save the plot BEFORE showing it
output_dir = "./outputs/figures"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'laptop_price_plot.png'))

# Now show the plot
plt.show()
