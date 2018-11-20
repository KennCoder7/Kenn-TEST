import numpy as np
import pandas as pd

labels = np.array(['Cat', 'Dog', 'Dog', 'Cat', 'Bird', 'Fish'])
print("Labels shape: %d" % labels.shape)
print("Labels:", labels)

print(pd.get_dummies(labels))
one_hot = np.asarray(pd.get_dummies(labels))
print("One-hot Labels shape:", one_hot.shape)
print("One-hot Labels:", '\n', one_hot)
