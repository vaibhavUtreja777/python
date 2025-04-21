# Practical 12: Over-fitting and Regularization
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Generate noisy dataset
np.random.seed(42)
X = np.sort(5 * np.random.rand(20, 1), axis=0)  # 20 points, 0 to 5
y = 2 + 3 * X + 2 * X**2 + np.random.randn(20, 1)  # Quadratic with noise
X = X.reshape(-1, 1)  # Ensure 2D for sklearn
y = y.ravel()  # Flatten for sklearn

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("Training Data Points:", len(X_train))
print("Test Data Points:", len(X_test))

# Part 1: Linear Regression (simple model)
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_train_pred_lin = lin_reg.predict(X_train)
y_test_pred_lin = lin_reg.predict(X_test)
train_mse_lin = mean_squared_error(y_train, y_train_pred_lin)
test_mse_lin = mean_squared_error(y_test, y_test_pred_lin)
print("\nLinear Regression:")
print(f"Training MSE: {train_mse_lin:.2f}")
print(f"Test MSE: {test_mse_lin:.2f}")

# Part 2: Polynomial Regression (over-fitting)
degree = 10
polyreg = make_pipeline(PolynomialFeatures(degree), LinearRegression())
polyreg.fit(X_train, y_train)
y_train_pred_poly = polyreg.predict(X_train)
y_test_pred_poly = polyreg.predict(X_test)
train_mse_poly = mean_squared_error(y_train, y_train_pred_poly)
test_mse_poly = mean_squared_error(y_test, y_test_pred_poly)
print("\nPolynomial Regression (degree 10):")
print(f"Training MSE: {train_mse_poly:.2f}")
print(f"Test MSE: {test_mse_poly:.2f}")

# Part 3: Ridge Regression (regularized polynomial)
ridge_poly = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=1.0))
ridge_poly.fit(X_train, y_train)
y_train_pred_ridge = ridge_poly.predict(X_train)
y_test_pred_ridge = ridge_poly.predict(X_test)
train_mse_ridge = mean_squared_error(y_train, y_train_pred_ridge)
test_mse_ridge = mean_squared_error(y_test, y_test_pred_ridge)
print("\nRidge Regression (degree 10, regularized):")
print(f"Training MSE: {train_mse_ridge:.2f}")
print(f"Test MSE: {test_mse_ridge:.2f}")

# Plot all models
X_plot = np.linspace(0, 5, 100).reshape(-1, 1)
plt.figure(figsize=(8, 5))
plt.scatter(X_train, y_train, color="blue", label="Training Data")
plt.scatter(X_test, y_test, color="green", label="Test Data")
plt.plot(X_plot, lin_reg.predict(X_plot), color="red", label="Linear Regression")
plt.plot(X_plot, polyreg.predict(X_plot), color="orange", label=f"Polynomial (degree {degree})")
plt.plot(X_plot, ridge_poly.predict(X_plot), color="purple", label="Ridge Regression")
plt.title("Over-fitting vs. Regularization")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.savefig("overfitting_regularization.png")  # Save for screenshot
plt.show()