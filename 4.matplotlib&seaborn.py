# Practical 4: Data Visualization with Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data
data = {
    "X": [1, 2, 3, 4, 5],
    "Y": [10, 20, 25, 30, 40],
    "Category": ["A", "B", "C", "D", "E"],
    "Values": [15, 25, 20, 30, 10]
}
df = pd.DataFrame(data)

# Part 1: Matplotlib - Line Plot
print("Creating Matplotlib Line Plot...")
plt.figure(figsize=(6, 4))
plt.plot(df["X"], df["Y"], marker="o", color="blue", linestyle="-")
plt.title("Line Plot with Matplotlib")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.savefig("line_plot.png")  # Save for screenshot
plt.show()

# Part 2: Matplotlib - Scatter Plot
print("Creating Matplotlib Scatter Plot...")
plt.figure(figsize=(6, 4))
plt.scatter(df["X"], df["Y"], color="red", s=100)
plt.title("Scatter Plot with Matplotlib")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)
plt.savefig("scatter_plot.png")  # Save for screenshot
plt.show()

# Part 3: Seaborn - Bar Plot
print("Creating Seaborn Bar Plot...")
plt.figure(figsize=(6, 4))
sns.barplot(x="Category", y="Values", data=df, hue="Category", palette="viridis", legend=False)
plt.title("Bar Plot with Seaborn")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.savefig("bar_plot.png")  # Save for screenshot
plt.show()