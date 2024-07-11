#Pandas Read CSV

import pandas as pd

df = pd.read_csv('/home/ubantu/Desktop/Desktop/ubantu@ubantu-1-0_~_Desktop_rental-core-engine\$ git checkout.docx.csv')
print(df.to_string())


#Tip: use to_string() to print the entire DataFrame.

import pandas as pd

df = pd.read_csv('/home/ubantu/Desktop/Desktop/ubantu@ubantu-1-0_~_Desktop_rental-core-engine\$ git checkout.docx.csv')
print(df) 


#---------------------------------------------------------------



#max_rows

print(pd.options.display.max_rows)  



#-------------------------------------------------------------------------



import pandas as pd

pd.options.display.max_rows = 9999
df = pd.read_csv('/home/ubantu/Desktop/Desktop/ubantu@ubantu-1-0_~_Desktop_rental-core-engine\$ git checkout.docx.csv')
print(df) 