# Practical 7: NumPy Array Operations (with loc and iloc)
import pandas as pd
import numpy as np
import time

# Part 1: Create a Pandas DataFrame
data = {
    "A": [6, 4, 2],
    "B": [3, 6, 6],
    "C": [7, 9, 7]
}
df = pd.DataFrame(data, index=["Row1", "Row2", "Row3"])
print("Pandas DataFrame:")
print(df)

# Part 2: Select elements using loc and iloc
print("\nSelecting Elements with loc and iloc:")
# Using loc (label-based)
first_row_loc = df.loc["Row1", :]
print("First Row (loc):")
print(first_row_loc)
# Select column 'B' for Row2 and Row3
column_b_loc = df.loc[["Row2", "Row3"], "B"]
print("Column B for Row2 and Row3 (loc):")
print(column_b_loc)

# Using iloc (integer-based)
element_iloc = df.iloc[1, 2]  # Row2, Column C
print("Element at position (1, 2) (iloc):", element_iloc)
# Select top-left 2x2 sub-dataframe
sub_df_iloc = df.iloc[:2, :2]
print("Top-left 2x2 Sub-DataFrame (iloc):")
print(sub_df_iloc)

# Part 3: Convert to NumPy array and perform operations
array_3x3 = df.to_numpy()
print("\nConverted to NumPy Array:")
print(array_3x3)

print("\nArray Operations:")
array_sum = np.sum(array_3x3)
array_mean = np.mean(array_3x3)
print("Sum of all elements:", array_sum)
print("Mean of all elements:", array_mean)

# Matrix multiplication
matrix_product = np.dot(array_3x3, array_3x3)
print("Matrix Multiplication (array * array):")
print(matrix_product)

# Part 4: Compare array vs list performance
print("\nComparing Array vs List Performance:")
large_list = list(range(1000000))
large_array = np.arange(1000000)

# Time list operation (sum)
start_time = time.time()
list_sum = sum(large_list)
list_time = time.time() - start_time
print(f"List sum time: {list_time:.4f} seconds")

# Time array operation (sum)
start_time = time.time()
array_sum = np.sum(large_array)
array_time = time.time() - start_time
print(f"Array sum time: {array_time:.4f} seconds")