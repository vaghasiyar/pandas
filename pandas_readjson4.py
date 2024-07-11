#Pandas Read JSON 

#Read JSON

import pandas as pd

df = pd.read_json('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.json')
print(df.to_string()) 



#--------------------------------------------------------------------



#Dictionary as JSON


import pandas as pd

data = {
  "Duration":{
    "0":100,
    "1":44,
    "2":425,
    "3":75,
    "4":95,
    "5":45
  },
  "Pulse":{
    "0":745,
    "1":758,
    "2":862,
    "3":456,
    "4":756,
    "5":742
  },
  "Maxpulse":{
    "0":486,
    "1":462,
    "2":952,
    "3":859,
    "4":852,
    "5":456
  },
  "Calories":{
    "0":425,
    "1":756,
    "2":894,
    "3":423,
    "4":785,
    "5":745
  }
}
df = pd.DataFrame(data)
print(df) 