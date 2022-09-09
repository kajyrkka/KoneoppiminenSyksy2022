import numpy as np
import matplotlib.pyplot as plt

'''
Kertauskysymyksiä:
1. Fs = 100Hz, mihin laskostuu 201Hz signaali ellei järjestelmässä ole antialias suodatinta
2. Jos käytetään 4 bittistä A/D-muunninta ja sisään menevä signaali skaalataan aina välille 1 ja -1 V,
   niin mikä on maksimi jännitevirhe, joka syntyy kvantisoinnissa?
3. Jos Fs = 1000 (df = Fs/N), ja lasket Fourier muunnoksesta kaksi ensimmäistä arvoa, niin mitä 
   taajuuksia nuo lukuarvot esittävät, jos lasket FFT:n 10000 näytteen yli?
4. Monenko aikatason näytteen yli sinun tulisi Fourier muunnos laskea, jotta toinen arvo esittäisi 2Hz
   taajuutta?
5. Entä monesko Fourier muunnoksen arvo esittää taajuutta 3Hz jos Fs edelleen 1000 ja Fourier muunnos
   lasketaan 4000 näytteen yli.

Värkätään vähän yhdessä Numpyllä näitä tietoliikenteen asioita.

1. Osoitetaan, että aikatasosta päästään taajuustasoon ja takaisin
2. Osoitetaan, että Fourier muunnoksen kompleksinen tulos tarkoittaa tietyn taajuista, amplitudista ja vaiheista
   kosini signaalia.
3. Näytetään kahden kosinisignaalin sekoitus
4. Näytetään taajuuden ja vaiheen korjaus kompleksisella signaalilla

'''

'''
4. Näytetään taajuuden ja vaiheen korjaus kompleksisella signaalilla
'''

Fs = 1000
Ts = 1/Fs
t = np.arange(0,1,Ts)
N = t.size
A = 2 # signaalin amplitudi
f = 4 # signaalin taajuus
V = 0 #np.pi/4 # signaalin vaihe
j = complex(0,1) # kompleksinen luku 0+j
s1 = A*np.exp(j*2*np.pi*f*t + V)
phaseShift = 1*np.exp(j*np.pi)
fshift = 20
freqShift = 1*np.exp(j*2*np.pi*fshift*t)

#repairedSignal = s1*phaseShift
repairedSignal = s1*freqShift



plt.figure(1)
plt.subplot(2,2,1),plt.plot(t,(s1.real)),plt.title("cos branch of complex vector")
plt.subplot(2,2,2),plt.plot(t,(s1.imag)),plt.title("sin branch of complex vector")

plt.subplot(2,2,3),plt.plot(t,(repairedSignal.real)),plt.title("cos branch of repaired")
plt.subplot(2,2,4),plt.plot(t,(repairedSignal.imag)),plt.title("sin branch of repaired")
plt.show()


'''
3. Näytetään kahden kosinisignaalin sekoitus



Fs = 1000
Ts = 1/Fs
t = np.arange(0,1,Ts)
N = t.size
f1 = 19
f2 = 21
s1 = np.cos(2*np.pi*f1*t)
s2 = np.cos(2*np.pi*f2*t)
tulo = s1*s2
print("Suurempi taajuuksista = 19+21 Hz = 40 Hz suodatetanpa se pois")
suodatin = (1/25)*np.ones(int((Fs/40)))
s3 = np.convolve(tulo,suodatin)
plt.figure(1)
plt.subplot(2,2,1),plt.plot(t,s1),plt.title('First signal')
plt.subplot(2,2,2),plt.plot(t,s2),plt.title('second signal')
plt.subplot(2,2,3),plt.plot(t,tulo),plt.title('product signal')
plt.subplot(2,2,4),plt.plot(s3),plt.title('filtered signal')
plt.show()

'''




'''
1. Osoitetaan, että aikatasosta päästään taajuustasoon ja takaisin
2. Osoitetaan, että Fourier muunnoksen kompleksinen tulos tarkoittaa tietyn taajuista, amplitudista ja vaiheista

'''
'''
Fs = 1000
Ts = 1/Fs
t = np.arange(0,1,Ts)
N = t.size
f = 5
fii = np.pi/4
sig = np.cos(2*np.pi*f*t + fii)

taajuustaso = np.fft.fft(sig)
print(taajuustaso[0:10] )

aikataso = np.real(np.fft.ifft(taajuustaso))

df = Fs/N
print("Fourier muunnoksen resoluutio = ", df, " Hz")
print("10 Hz piikki löytyy kohdasta 10 taajuustasosta = ", taajuustaso[f])
Amplitudi = np.abs(taajuustaso[f]/N)
Vaihe = np.angle(taajuustaso[f]/N)
sigFourier = 2*Amplitudi*np.cos(2*np.pi*f*t + Vaihe)


plt.figure(1)
plt.subplot(2,2,1)
plt.plot(t,sig)
plt.subplot(2,2,2)
plt.plot(np.abs(taajuustaso)/N)
plt.subplot(2,2,3)
plt.plot(aikataso)
plt.subplot(2,2,4)
plt.plot(sigFourier)
plt.show()

'''