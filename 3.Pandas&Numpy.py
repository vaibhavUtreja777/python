# Practical 3: Working with Pandas and NumPy
import pandas as pd
import numpy as np

# Part 1: Create a Pandas Series and DataFrame
students = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 90, 78, 92]
}

# Create DataFrame
df = pd.DataFrame(students)
print("\nStudent DataFrame:")
print(df)

# Create a Series from Marks column
marks_series = pd.Series(df["Marks"], name="Marks")
print("\nMarks Series:")
print(marks_series)

# Part 2: NumPy operations
# Convert Marks to NumPy array
marks_array = np.array(df["Marks"])
print("\nMarks Array:", marks_array)

# Perform basic operations
mean_marks = np.mean(marks_array)
max_marks = np.max(marks_array)
min_marks = np.min(marks_array)

print(f"Mean Marks: {mean_marks}")
print(f"Maximum Marks: {max_marks}")
print(f"Minimum Marks: {min_marks}")

# Additional NumPy operation: Square the array
squared_marks = np.square(marks_array)
print("\nSquared Marks Array:", squared_marks)