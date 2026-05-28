import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv( r"D:\DS_PRACTICE\28-05-2026\logistic classification.csv")

X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, -1].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
#for this observation let me selcted as 100 observaion for test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20,random_state=0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler() 
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test) 
#we mentioned feature scaling only to independent variable not dependent variable at all

# Training the SVM Model on the traing set
from sklearn.svm import SVC
classifier = SVC()
classifier.fit(X_train,y_train)



# # Making the confusion Matrix
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(y_test,y_pred)
# print(cm)

# # KNN classifer algorithm
# from sklearn.neighbors import KNeighborsClassifier
# classifier_knn = KNeighborsClassifier
# classifier_knn.fit(X_train, y_train)

# Prediction the Test set Result
y_pred = classifier.predict(X_test)

#making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print("confusion_matrix =",cm)

# this is to get the Model Accuracy
from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print("accuracy_score=",ac)

ac1 = classifier.score(X_test, y_test)
print("accuracy =",ac1)


bias = classifier.score(X_train,y_train)
print("bias=",bias)

# This is to get the Classification Report
from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
print("classification_report =",cr)


variance = classifier.score(X_test, y_test)
print("variance=",variance)

# import seaborn as sns

# sns.heatmap(cm, annot=True)
# plt.savefig("outputs/confusion_matrix.png")
# plt.show()