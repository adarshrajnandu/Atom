import pandas as pd

from Data_Preparation import *
print(obj_df['drive_wheels'])

#convert each category values into a new column and assign 1 and 0

#the new dataset contains three columns drive_wheels_4wd, drive_wheels_fwd and
#drive_wheels_rwd

pd.get_dummies(obj_df, columns = ['body_style','drive_wheels'],
prefix = ['body','drive']).head()

#get_dummies returns the full dataframe so we need to filter out the objects
#using select_dtypes
