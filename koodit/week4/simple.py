import numpy as np
import matplotlib.pyplot as plt

'''
Tehdään vielä yksinkertainen

'''
X = 1
Y = np.power(X,2)
x = np.linspace(-5,5,100)
y= np.power(x,2)
rate = 0.9
for i in range(10):
    plt.figure(1)
    plt.subplot(5,2,i+1),plt.plot(x,y),plt.plot(X,Y,'*r')
    X = X - (2*X)*rate
    Y = np.power(X,2)
    
    #plt.pause(1)
plt.show()


