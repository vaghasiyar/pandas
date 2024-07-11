# DataFrames

import pandas as pd

data = {
  "Name": ["Rahul","Het", "raj"],
  "Salary": [100000,50000,80000]
}
data2 = pd.DataFrame(data)
print(data2)


#-----------------------------

#Locate Row
print(data2.loc[[1]])

print(data2.loc[[2,0]])


#--------------------------------


#Named Indexes
data2 = pd.DataFrame(data,index = ["day1", "day2", "day3"])
print(data2)



#-----------------------------------------

# Locate Named Indexes
print(data2.loc["day2"])



