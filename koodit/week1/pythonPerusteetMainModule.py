'''
 Tämän ja pythonPerusteetMain.py tiedoston tavoittena on:
 1) esittää mikä on python moduli
 2) miten tuo moduli = skripti voi toimia itsenäisenä "main" ohjelmana tai olla osa suurempaa kokonaisuutta.
'''
import numpy as np
import matplotlib.pyplot as plt

def plot(x,y):
    plt.figure(1)
    plt.plot(x,y,'-*')
    plt.show()

def makeSignal():
    Fs = 1000.0           # Sampling frequency
    Ts = 1/Fs             # Sampling time interval
    f = 5                 # signal frequency
    #t = np.arange(start=0,stop=1,step=Ts)       # numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
    t = np.arange(0,1,Ts)       # numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
    sig = np.cos(2*np.pi*f*t)
    return t,sig


if __name__ == '__main__':
    x,y = makeSignal()
    plot(x,y)
