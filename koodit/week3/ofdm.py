import numpy as np
import matplotlib.pyplot as plt

taajuustaso = np.zeros(128,dtype=complex)

#moduloidaan yksi 128:sta kantoaallosta

taajuustaso[4] = complex(1,1)
taajuustaso[24] = complex(1,1)

aikataso = np.fft.ifft(taajuustaso)

plt.figure(1)
plt.subplot(2,2,1),plt.plot(abs(taajuustaso)),plt.title('taajuustaso')
plt.subplot(2,2,3),plt.plot(np.real(aikataso)),plt.title('I haara = kosinihaara')
plt.subplot(2,2,4),plt.plot(np.imag(aikataso)),plt.title('Q haara = sinihaara')
plt.show()