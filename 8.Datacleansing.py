# Practical 8: Data Cleansing and Normalization
import pandas as pd
import numpy as np

# Create a sample DataFrame with missing values and duplicates
data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", "Eve", "Bob"],
    "Age": [25, np.nan, 22, 25, 30, np.nan],
    "Salary": [50000, 60000, 45000, 50000, np.nan, 60000]
}
df = pd.DataFrame(data)
print("Original DataFrame with missing values and duplicates:")
print(df)

# Step 1: Remove duplicates
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)

# Step 2: Fill missing values with column mean
df_cleaned = df_no_duplicates.copy()
df_cleaned["Age"] = df_cleaned["Age"].fillna(df_cleaned["Age"].mean())
df_cleaned["Salary"] = df_cleaned["Salary"].fillna(df_cleaned["Salary"].mean())
print("\nDataFrame after filling missing values with mean:")
print(df_cleaned)

# Step 3: Normalize the Salary column (scale to 0-1)
salary_min = df_cleaned["Salary"].min()
salary_max = df_cleaned["Salary"].max()
df_cleaned["Salary_Normalized"] = (df_cleaned["Salary"] - salary_min) / (salary_max - salary_min)
print("\nDataFrame with normalized Salary column:")
print(df_cleaned)