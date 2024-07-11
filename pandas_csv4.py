# Pandas - Cleaning Empty Cells


#Remove Rows

import pandas as pd

df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
new_df = df.dropna()
print(new_df.to_string())



#If you want to change the original DataFrame, use the inplace = True argument:


df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
df.dropna(inplace = True)
print(df.to_string()) 


#Replace Empty Values

df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
df.fillna('pythonmoduls', inplace = True) 


#Replace Only For Specified Columns

df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
df["Calories"].fillna('pythonmoduls', inplace = True)
print(df.to_string())




#---------------------------------------------------------------------------------------------



#Pandas - Cleaning Data of Wrong 


#Pandas has a to_datetime() method for this:


import pandas as pd
df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())




#------------------------------------------------------------------------------------------------------------


#Pandas - Fixing Wrong Data


#Replacing Values


import pandas as pd

df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
df.loc[2,'Duration'] = 7
print(df.to_string())



df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 56:
    df.loc[x, "Duration"] = 52
print(df.to_string())



#Removing Rows

df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
print(df.to_string())






#----------------------------------------------------------------------------------------

#Pandas - Removing Duplicates


#The duplicated() method returns a Boolean values for each row:
import pandas as pd

df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
print(df.duplicated())


