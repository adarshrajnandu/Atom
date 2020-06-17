import pandas as pd
import numpy as np

# Define the headers since the data does not have any
headers = ["symboling", "normalized_losses", "make", "fuel_type", "aspiration",
           "num_doors", "body_style", "drive_wheels", "engine_location",
           "wheel_base", "length", "width", "height", "curb_weight",
           "engine_type", "num_cylinders", "engine_size", "fuel_system",
           "bore", "stroke", "compression_ratio", "horsepower", "peak_rpm",
           "city_mpg", "highway_mpg", "price"]

# Read in the CSV file and convert "?" to NaN
df = pd.read_csv("http://mlr.cs.umass.edu/ml/machine-learning-databases/autos/imports-85.data",
                  header=None, names=headers, na_values="?" )
df.head()

df.dtypes

#select those columns whose datatype is "object"
obj_df = df.select_dtypes(include = ['object']).copy()
obj_df.head()

#clean up null values
obj_df[obj_df.isnull().any(axis=1)]

obj_df["num_doors"].value_counts()
obj_df = obj_df.fillna({"num_doors": "four"})
