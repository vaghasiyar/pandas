#Pandas - Data Correlations


#Finding Relationships

import pandas as pd

df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
print(df.corr())
