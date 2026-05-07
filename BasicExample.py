# Import libraries
import pandas as pd
import numpy as np

# Import train-test split function
from sklearn.model_selection import train_test_split

# Import Linear Regression model
from sklearn.linear_model import LinearRegression

# -------------------------------
# STEP 1: Create Dataset
# -------------------------------

# Sample data
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8],
    'Marks': [10, 20, 30, 40, 50, 60, 70, 80]
}

# Convert into DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -------------------------------
# STEP 2: Define X and Y
# -------------------------------

# Independent variable
X = df[['Hours']]

# Dependent variable
Y = df['Marks']

# -------------------------------
# STEP 3: Split Data
# -------------------------------

x_train, x_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=0
)

# -------------------------------
# STEP 4: Create Model
# -------------------------------

regressor = LinearRegression()

# -------------------------------
# STEP 5: Train Model
# -------------------------------

regressor.fit(x_train, y_train)

print("\nModel Trained Successfully")

# Learned relationship:

print("Hello")

::contentReference[oaicite:0]{index=0}


# -------------------------------
# STEP 6: Predict Values
# -------------------------------

y_pred = regressor.predict(x_test)

# -------------------------------
# STEP 7: Compare Results
# -------------------------------

comparison = pd.DataFrame({
    'Actual': y_test,
    'Predicted': y_pred
})

print("\nActual vs Predicted:")
print(comparison)

# -------------------------------
# STEP 8: Predict New Value
# -------------------------------

new_value = [[9]]

prediction = regressor.predict(new_value)

print("\nPrediction for 9 hours:")
print(prediction)