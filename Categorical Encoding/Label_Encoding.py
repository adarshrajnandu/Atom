#different values of a column are labelled using numbers

from Data_Preparation import *
obj_df['body_style'] = obj_df['body_style'].astype('category')
obj_df.dtypes

obj_df['body_style_cat'] = obj_df['body_style'].cat.codes
print(obj_df.head())
