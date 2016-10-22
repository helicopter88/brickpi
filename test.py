import matplotlib.pyplot as plt 
import numpy as np
plt.plot(*np.loadtxt("log.txt",unpack=True, usecols={0,4}), linewidth=2.0, label="act_1")
#plt.plot(*np.loadtxt("log.txt",unpack=True, usecols={0,2}), linewidth=2.0, label="act_0")
plt.plot(*np.loadtxt("log.txt",unpack=True, usecols={0,3}), linewidth=2.0, label="ref_1")
#plt.plot(*np.loadtxt("log.txt",unpack=True, usecols={0,1}), linewidth=2.0, label="ref_0")
plt.legend()
plt.show()
