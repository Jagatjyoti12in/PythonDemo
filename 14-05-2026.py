import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('C:\\Users\\Jagatjyoti\\Jagat_Code\\14-05-2026\\emp_sal.csv')
# dataset = pd.read_csv('./emp_sal.csv')
dataset.head()

x= dataset.iloc[:,1:2].values
y= dataset.iloc[:,2].values

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x,y)

plt.scatter(x,y,color='red')
plt.plot(x,lin_reg.predict(x),color='blue')
plt.title('Salary vs Experience (Linear Regression)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
lin_reg.predict([[6.5]])
lin_reg.fit(x,y)

#Polynomial Regression

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
x_poly = poly_reg.fit_transform(x)

poly_reg.fit(x_poly,y)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly,y)     

plt.scatter(x,y,color='red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Salary vs Experience (Polynomial Regression)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_model_pred)


