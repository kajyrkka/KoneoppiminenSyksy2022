import numpy as np
import matplotlib.pyplot as plt

'''
Palautetaanpa vielä mieleen miten Fourier-muunnos toimii
Kaavat löytyy https://en.wikipedia.org/wiki/Discrete_Fourier_transform
Ja nyt kun kerran ollaan opittu työkalu (Python/Numpy/Matlotlib), meillä
on välineet asioiden opettelemiseen myös itsenäisesti insinöörimäisesti
kokeilemalla asioita. Eli Aloitetaan kokeilemaan...
'''

# Muodostetaan ensin joku tunnettu signaali, jonka näytteista lasketaan
# Fourier muunnos
Fs = 1000; Ts = 1/Fs; t = np.arange(0,1,Ts)
s1 = np.sin(2*np.pi*1*t)
s2 = (1/3)*np.sin(2*np.pi*3*t)
s3 = (1/5)*np.sin(2*np.pi*5*t)
s4 = (1/7)*np.sin(2*np.pi*7*t)
s5 = (1/9)*np.sin(2*np.pi*9*t)
summa = s1 + s2 + s3 + s4 + s5
N = len(t)
print("Taajuusresoluutio on nyt = ", Fs/N)
df = int(Fs/N)

s1fft = (np.fft.fft(summa))/N
print("s1fft dtype = ", s1fft.dtype)

s1fftposit = s1fft[0:int(N/2)+1]
fakseli = np.arange(0,int(Fs/2)+df,df)
print("fakseli shape = ", fakseli.shape)
print("s1fftposit shape = ", s1fftposit.shape)

plt.figure(1)
plt.subplot(2,2,1),plt.plot(t,summa),plt.title("aikatason signaali")
plt.subplot(2,2,2),plt.plot(fakseli,s1fftposit.real),plt.title("real part")
plt.subplot(2,2,3),plt.plot(fakseli,s1fftposit.imag),plt.title("imaginary part")
plt.subplot(2,2,4),plt.plot(fakseli,abs(s1fftposit)),plt.title("abs real+imag")
plt.show()
