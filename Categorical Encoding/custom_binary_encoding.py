import numpy  as np
from Data_Preparation import *

print(obj_df['engine_type'].value_counts())

#if all the variations of OHC are same for the analysis

obj_df['OHC_CODE'] = np.where(obj_df['engine_type'].str.contains('ohc'),1,0)

print(obj_df[['make','engine_type','OHC_CODE']].head())
