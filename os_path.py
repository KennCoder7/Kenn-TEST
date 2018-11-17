import os
import numpy as np

data = np.array([1, 2, 3])
if not os.path.exists("./data/"):
    print("# path not exists")
    os.makedirs("./data/")
    if not os.path.exists("./data/data.npy"):
        print("# data.npy not exists")
        np.save("./data/data.npy", data)

print("# path exists? :", os.path.exists("./data/"))
print("# data.npy exists? :", os.path.exists("./data/data.npy"))