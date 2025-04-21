# Practical 6: Pandas DataFrame Operations
import pandas as pd

# Step 1: Create a sample .csv file
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [24, 28, 22, 30, 27],
    "Salary": [50000, 60000, 45000, 70000, 55000]
}
df = pd.DataFrame(data)
df.to_csv("employees.csv", index=False)
print("Created employees.csv")

# Step 2: Import the .csv file
df = pd.read_csv("employees.csv")
print("\nOriginal DataFrame:")
print(df)

# Step 3: Filter rows where Age > 25
filtered_df = df[df["Age"] > 25]
print("\nFiltered DataFrame (Age > 25):")
print(filtered_df)

# Step 4: Add a new column for 10% salary raise
df["New_Salary"] = df["Salary"] * 1.1
print("\nDataFrame with New Salary Column:")
print(df)

# Step 5: Export modified DataFrame to a new .csv
df.to_csv("employees_modified.csv", index=False)
print("\nExported modified DataFrame to employees_modified.csv")