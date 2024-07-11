#Pandas - Analyzing DataFrames

#Viewing the Data

import pandas as pd

df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
print(df.head(10)) 


#The head() method returns the headers and a specified number of rows, starting from the top.

df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
print(df.head()) 



#There is also a tail() method for viewing the last rows of the DataFrame.
#The tail() method returns the headers and a specified number of rows, starting from the bottom


df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')

print(df.tail())

