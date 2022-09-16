import numpy as np
import matplotlib.pyplot as plt

Fs = 1000
Ts = 1/Fs
t = np.arange(0,1,Ts)
d1 = np.ones(500)
d0 = -np.ones(500)
cosData = d1
sinData = np.ones(1000)
cosData = np.hstack((cosData,d0))
cosData = np.hstack((cosData,d1))
cosData = np.hstack((cosData,d0))
sinData =np.hstack((sinData,-np.ones(1000)))
f = 3
j = complex(0,1)
phasor = np.exp(j*2*np.pi*f*t)

x = np.real(phasor)#*cosData
y = np.imag(phasor)#*sinData

ax = plt.axes(projection = '3d')
ax.plot3D(x,y,t,'-.r')
plt.show()
