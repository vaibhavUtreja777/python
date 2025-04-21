# Practical 9: Advanced Visualization (with Heatmap)
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Create sample dataset with numeric variables for heatmap
data = {
    "Category": ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "D"],
    "Values": [23, 25, 27, 30, 28, 32, 19, 22, 20, 35, 33, 34],
    "Feature1": [10, 12, 11, 15, 14, 16, 8, 9, 7, 18, 17, 19],
    "Feature2": [5, 6, 4, 8, 7, 9, 3, 2, 4, 10, 11, 12]
}
df = pd.DataFrame(data)
print("Sample Dataset:")
print(df)
# Set Seaborn style
sns.set_style("whitegrid")
# Part 1: Histogram
print("\nCreating Histogram...")
plt.figure(figsize=(6, 4))
sns.histplot(data=df, x="Values", bins=10, color="skyblue")
plt.title("Histogram of Values")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.savefig("histogram.png")  # Save for screenshot
plt.show()
# Part 2: Boxplot
print("\nCreating Boxplot...")
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="Category", y="Values", hue="Category", palette="Set2", legend=False)
plt.title("Boxplot by Category")
plt.xlabel("Category")
plt.ylabel("Values")
plt.savefig("boxplot.png")  # Save for screenshot
plt.show()
# Part 3: Heatmap (correlation matrix)
print("\nCreating Heatmap...")
# Select numeric columns for correlation
numeric_df = df[["Values", "Feature1", "Feature2"]]
corr_matrix = numeric_df.corr()
plt.figure(figsize=(6, 4))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")  # Save for screenshot
plt.show()