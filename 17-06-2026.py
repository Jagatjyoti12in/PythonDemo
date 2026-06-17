print("17-06-2026")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk

# Download stopwords once
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Load Dataset
dataset = pd.read_csv(
    r"D:\DS_PRACTICE\17-06-2026\Restaurant_Reviews.tsv",
    delimiter='\t',
    quoting=3
)

# Text Cleaning
corpus = []
ps = PorterStemmer()

for i in range(0, len(dataset)):
    
    # Remove non-alphabetic characters
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])

    # Convert to lowercase
    review = review.lower()

    # Tokenize
    review = review.split()

    # Stemming and Stopword Removal
    review = [
        ps.stem(word)
        for word in review
        if word not in set(stopwords.words('english'))
    ]

    # Join words back into sentence
    review = ' '.join(review)

    corpus.append(review)

# Bag of Words
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=1500)
X = cv.fit_transform(corpus).toarray()

# Dependent Variable
y = dataset.iloc[:, 1].values

# Train-Test Split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Model Training
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", round(accuracy * 100, 2), "%")