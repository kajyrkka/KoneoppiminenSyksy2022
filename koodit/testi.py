import numpy as np
import matplotlib.pyplot as plt

Fs = 10;
Ts = 1/Fs;
t = np.arange(0,1,Ts)

sig1 = np.cos(2*np.pi*1*t)
sig2 = np.cos(2*np.pi*2*t)
print("signaalin koko = ",sig1.shape)

plt.figure(1)
plt.subplot(2,2,1)
plt.plot(t,sig1)

plt.subplot(2,2,4)
plt.plot(t,sig1)

plt.show()
