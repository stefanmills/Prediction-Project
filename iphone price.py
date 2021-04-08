import pandas as pd
from sklearn.linear_model import LinearRegression
data=pd.read_csv('iphoneprices.csv')
model= LinearRegression()
model.fit(data[['MODEL']],data[['PRICE($)']])
print(model.predict([[1]]))
