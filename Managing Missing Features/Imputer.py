from sklearn.impute import SimpleImputer
import numpy as np

data = np.array([[1,np.nan,2],[2,3,np.nan],[np.nan,4,5]])
print(data)

imp_mean = SimpleImputer(strategy = 'mean')
print(imp_mean.fit_transform(data))

imp_median = SimpleImputer(strategy = 'median')
print(imp_median.fit_transform(data))

imp_freq = SimpleImputer(strategy = 'most_frequent')
print(imp_freq.fit_transform(data))
