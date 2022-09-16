import numpy as np
import matplotlib.pyplot as plt

j = complex(0,1)
s = 1+j
print("Lähetetään symboli = ", s)

# Kun signaali menee kanava läpi sen vaihe ja amplitudi muuttuu
h = 0+ 0.5*j   # vaihe kääntyy +90 astetta ja amplitudi vaimenee

r = s*h
print("vastaanotettiin symboli = ",r)

# Miten tämä voidaan korjata? Kertomalla vastaanotettu signaali

korjattu = r*h.conjugate()
print("vaihe korjattu symboli = ", korjattu)

korjattu = korjattu/(abs(h)*abs(h))
print("vaihe ja amplitudikorjattu symboli = ", korjattu)

taajuustaso = np.zeros(10,dtype=complex)

taajuustaso[1] = complex(1,1)
taajuustaso[4] = complex(-1,-1)

aikataso = np.fft.ifft(taajuustaso)
plt.figure()
plt.subplot(2,1,1),plt.plot(np.real(aikataso))
plt.subplot(2,1,2),plt.plot(np.imag(aikataso))
plt.show()

vastaanotettu = np.fft.fft(aikataso)
print(vastaanotettu)