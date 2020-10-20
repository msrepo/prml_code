import numpy as np
import matplotlib.pyplot as plt

z = np.random.uniform(100)
y = np.tan(np.pi * z)
count,bins,_ = plt.hist(y,10,range=(0,1),density=True)
plt.show()

