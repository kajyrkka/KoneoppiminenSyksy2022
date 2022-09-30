import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
Ts = 1/Fs
t = np.arange(0,1,Ts)

s = np.cos(2*np.pi*1010*t)

plt.figure(1)
plt.stem(s[0:100])
plt.show()
