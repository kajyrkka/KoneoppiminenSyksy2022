'''
Harjoitellaan Pythonin toistorakenteita ja opetellaan samalla Fourier muunnoksen toimintaa
'''

import numpy as np
import matplotlib.pyplot as plt




'''
Let's make first a signal with 2 cosines at different frequencies 
and let's add some noise too.
'''
Fs = 1000
Ts = 1/Fs
t = np.arange(0,1,Ts)
s1 = np.cos(2*np.pi*10*t)
s2 = np.cos(2*np.pi*100*t)
n = 0.001*np.random.randn(t.size)

sig = s1+s2+n

freqContent = np.fft.fft(sig)
normFreqContent = freqContent/(t.size)
absFreqContent = np.abs(normFreqContent)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t,sig)
plt.subplot(2,1,2)
plt.plot(np.abs(absFreqContent))
plt.show()
