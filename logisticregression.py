import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve
)

dataset1 =pd.read_csv(r"D:\DS_PRACTICE\27-05-2026\Future prediction.csv")

X = dataset1.iloc[:, [2,3]].values
y = dataset1.iloc[:, 4].values

print(X)
print(y)
d2 = dataset1.copy()
dataset1 = dataset1.iloc[:,[2,3]].values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
M = sc.fit_transform(dataset1)

y_pred1 = pd.DataFrame()
d2['y_pred1'] = classifier.predict(M)
d2.to_csv('final1.csv')


from sklearn.metrics import roc_auc_score, roc_curve
y_pred_prob = classifier.predict_proba(X_test)[:,1]
auc_score = roc_auc_score(y_test, y_pred_prob)

auc_score

fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

plt.figure(figsize=(8,6))
plt.plot(fpr,tpr, label= f'Logistic Regression (AUC = {auc_score : .2f})')
plt.plot([0,1],[0,1], 'k--') # Random classifier line
plt.xlabel("False postive rate")
plt.ylabel("True positive rate")
plt.title("ROC Curve")
plt.grid()
plt.show()



