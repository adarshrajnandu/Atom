import numpy as np

x = np.random.uniform(0.0,1.0,size = (10,2))
y = np.random.choice(('Male','Female'), size = (10))

print(x[0])
print(y[0])

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
yt = le.fit_transform(y)

print(y)
print(yt)

#the inverse transformation
output = [1,1,0,1,0,0,1]
decoded_output = [le.classes_[i] for i in output]
print(decoded_output)


#one-hot encoding  (binarizer)
