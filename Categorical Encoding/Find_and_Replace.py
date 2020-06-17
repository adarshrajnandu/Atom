#replace values of columns that are used to represent words

from Data_Preparation import *
print(obj_df["num_cylinders"].value_counts())

cleanup_nums = {'num_doors': {'four':4, 'two':2},
                'num_cylinders': {'four':4,'six':6,'five':5,'eight':8,'two':2,
                'twelve':12,'three':3}}

obj_df.replace(cleanup_nums,inplace = True)
print(obj_df.head())
print(obj_df.dtypes)
