# Practical 10: Linear Regression with Scikit-Learn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create sample dataset (house sizes vs. prices)
data = {        "Size": [600, 800, 1000, 1200, 1400, 1600, 1800, 2000],
                "Price": [150000, 180000, 210000, 240000, 280000, 310000, 340000, 370000]}
df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Prepare data
X = df[["Size"]].values  # Features (2D array for sklearn)
y = df["Price"].values   # Target

# Train linear regression model
model = LinearRegression()
model.fit(X, y)
print("\nModel Coefficients:")
print(f"Slope: {model.coef_[0]:.2f}, Intercept: {model.intercept_:.2f}")

# Make predictions
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Predict for new sizes
new_sizes = np.array([[700], [1500]])
new_predictions = model.predict(new_sizes)
print("\nPredictions for new sizes:")
for size, pred in zip([700, 1500], new_predictions):
    print(f"Size: {size} sq ft, Predicted Price: ${pred:.2f}")

# Plot regression line
plt.figure(figsize=(6, 4))
plt.scatter(df["Size"], df["Price"], color="blue", label="Data")
plt.plot(df["Size"], y_pred, color="red", label="Regression Line")
plt.title("Linear Regression: House Size vs. Price")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($)")
plt.legend()
plt.savefig("linear_regression.png")  # Save for screenshot
plt.show()