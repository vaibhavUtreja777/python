# Practical 11: Logistic Regression with Scikit-Learn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Create sample dataset (student marks vs. pass/fail)
data = {
    "Marks": [35, 45, 55, 65, 75, 85, 95, 25, 50, 70],
    "Pass": [0, 0, 1, 1, 1, 1, 1, 0, 0, 1]  # 0 = Fail, 1 = Pass
}
df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Prepare data
X = df[["Marks"]].values  # Features
y = df["Pass"].values     # Target

# Train logistic regression model
model = LogisticRegression()
model.fit(X, y)
print("\nModel Coefficients:")
print(f"Slope: {model.coef_[0][0]:.2f}, Intercept: {model.intercept_[0]:.2f}")

# Make predictions
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)
conf_matrix = confusion_matrix(y, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)

# Predict for new marks
new_marks = np.array([[40], [80]])
new_predictions = model.predict(new_marks)
print("\nPredictions for new marks:")
for marks, pred in zip([40, 80], new_predictions):
    print(f"Marks: {marks}, Predicted Outcome: {'Pass' if pred == 1 else 'Fail'}")

# Plot decision boundary
plt.figure(figsize=(6, 4))
plt.scatter(df["Marks"], df["Pass"], color="blue", label="Data")
# Plot logistic curve
X_range = np.linspace(20, 100, 100).reshape(-1, 1)
y_prob = model.predict_proba(X_range)[:, 1]
plt.plot(X_range, y_prob, color="red", label="Logistic Curve")
plt.axvline(x=-(model.intercept_[0] / model.coef_[0][0]), color="green", linestyle="--", label="Decision Boundary")
plt.title("Logistic Regression: Marks vs. Pass/Fail")
plt.xlabel("Marks")
plt.ylabel("Probability of Passing")
plt.legend()
plt.savefig("logistic_regression.png")  # Save for screenshot
plt.show()