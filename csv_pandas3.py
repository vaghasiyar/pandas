# importing pandas module 
import pandas as pd 

# making data frame 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 

# calling tail() method 
# storing in new variable 
data_bottom = data.tail() 

# display 
data_bottom 
