#Pandas - Plotting

#Pandas uses the plot() method to create diagrams.

import sys
import matplotlib
matplotlib.use('Agg')



import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
df.plot()
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()







#-----------------------------------------------------------------------------


#Scatter Plot



"""

Specify that you want a scatter plot with the kind argument:

kind = 'scatter'

A scatter plot needs an x- and a y-axis.

In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.

Include the x and y arguments like this:

x = 'Duration', y = 'Calories'
"""


df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()




df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show() 





#---------------------------------------------------------------------------------------------

#Histogram

"""

Use the kind argument to specify that you want a histogram:

kind = 'hist'

A histogram needs only one column.

A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?

In the example below we will use the "Duration" column to create the histogram:

"""

df = pd.read_csv('file:///home/ubantu/Desktop/pythonmoduls/pandas_1/pandas/pandas2.py.csv')
df["Duration"].plot(kind = 'hist')
plt.show() 


