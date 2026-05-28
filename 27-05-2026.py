import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, LabelEncoder

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve
)

# -----------------------------------
# Load Dataset
# -----------------------------------

dataset1 = pd.read_csv( r"D:\DS_PRACTICE\27-05-2026\Future prediction.csv")

# Display dataset information
print("First 5 Rows:")
print(dataset1.head())

print("\nDataset Shape:")
print(dataset1.shape)

print("\nColumn Names:")
print(dataset1.columns)

# -----------------------------------
# Features and Target
# -----------------------------------

# Features -> Age and EstimatedSalary
X = dataset1.iloc[:, [2, 3]].values

# Target -> Gender
y = dataset1.iloc[:, 1].values

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)

# -----------------------------------
# Convert Male/Female into 0/1
# -----------------------------------

le = LabelEncoder()

y = le.fit_transform(y)

print("\nEncoded Target:")
print(y)

# -----------------------------------
# Train-Test Split
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=0,
    stratify=y
)

# -----------------------------------
# Feature Scaling
# -----------------------------------

sc = StandardScaler()

X_train = sc.fit_transform(X_train)

X_test = sc.transform(X_test)

# -----------------------------------
# Logistic Regression Model
# -----------------------------------

classifier = LogisticRegression()

# Train Model
classifier.fit(X_train, y_train)

# -----------------------------------
# Predictions
# -----------------------------------

y_pred = classifier.predict(X_test)

# -----------------------------------
# Model Evaluation
# -----------------------------------

print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -----------------------------------
# Predict on Full Dataset
# -----------------------------------

M = sc.transform(X)

predictions = classifier.predict(M)

# Convert predictions back to Male/Female
predicted_labels = le.inverse_transform(predictions)

d2 = dataset1.copy()

d2['y_pred1'] = predicted_labels

# Save CSV
d2.to_csv('final1.csv', index=False)

print("\nPrediction file saved as final1.csv")

# -----------------------------------
# ROC AUC and ROC Curve
# -----------------------------------

# Check if both classes exist in test data
if len(np.unique(y_test)) > 1:

    # Probability Predictions
    y_pred_prob = classifier.predict_proba(X_test)[:, 1]

    # AUC Score
    auc_score = roc_auc_score(y_test, y_pred_prob)

    print("\nAUC Score:")
    print(auc_score)

    # ROC Curve
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

    plt.figure(figsize=(8, 6))

    plt.plot(
        fpr,
        tpr,
        label=f'Logistic Regression (AUC = {auc_score:.2f})'
    )

    # Random Classifier Line
    plt.plot([0, 1], [0, 1], 'k--')

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")

    plt.title("ROC Curve")

    plt.legend()

    plt.grid()

    plt.show()

else:
    print("\nROC AUC cannot be calculated because only one class exists in y_test")