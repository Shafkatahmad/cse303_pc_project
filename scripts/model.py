import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("../data/raw/laptop_price.csv")

# Drop rows with missing values
df.dropna(inplace=True)

# transform string to numbers
label_encoders = {}  
for column in df.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le  # Save encoder for later use if needed

# Define target
if 'Price (Euro)' in df.columns:
    X = df.drop(columns=['Price (Euro)'])
    y = df['Price (Euro)']
else:
    raise ValueError("Target column 'Price (Euro)' not found in dataset")

# Split data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predict on test data
y_pred = lr_model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
print(f"Linear Regression Mean Squared Error: {mse:.2f}")
