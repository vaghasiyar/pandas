# Series

import pandas as pd
a = [1,2,3,4,5,6,7,8,9]
data = pd.Series(a)
print(data)


#----------------------------------------------------------

# index 
print(data[0])

#-------------------------------------------------------------

#Create Labels in index 

data = pd.Series(a, index = ["a","b","c","d","e","f","g","h","i"])
print(data)

# index 
print(data["c"]) 


#---------------------------------------------------------------


# Key/Value Objects as Series

data1= {"rahul": 420, "het": 380, "raj": 390}
data2 = pd.Series(data1)
print(data2)


#index 

data1= {"rahul": 420, "het": 380, "raj": 390}
data2 = pd.Series(data1, index = ["raj", "het"])
print(data2)