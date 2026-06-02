import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    classification_report
)

# Load Dataset
dataset = pd.read_csv(r"D:\DS_PRACTICE\02-06-2026\logistic classification.csv")

# Independent and Dependent Variables
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=0
)

# Feature Scaling
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Create Decision Tree Model
classifier = DecisionTreeClassifier(
    criterion='gini',      # or 'entropy'
    max_depth=5,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42
)

# Train Model
classifier.fit(X_train, y_train)

# Prediction
y_pred = classifier.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Accuracy Score
ac = accuracy_score(y_test, y_pred)
print("\nAccuracy Score =", ac)

# Test Accuracy
test_accuracy = classifier.score(X_test, y_test)
print("Test Accuracy =", test_accuracy)

# Training Accuracy
train_accuracy = classifier.score(X_train, y_train)
print("Training Accuracy =", train_accuracy)

# Bias
bias = 1 - train_accuracy
print("Bias =", bias)

# Variance
variance = train_accuracy - test_accuracy
print("Variance =", variance)

# Classification Report
cr = classification_report(y_test, y_pred)
print("\nClassification Report:")
print(cr)

# Model Evaluation
if variance > 0.10:
    print("Model Status: Overfitting")
elif train_accuracy < 0.80 and test_accuracy < 0.80:
    print("Model Status: Underfitting")
else:
    print("Model Status: Good Fit")