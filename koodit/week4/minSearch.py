import numpy as np
import matplotlib.pyplot as plt

'''
Tehdään vielä simulointi, miten seuraavat stepit toimikaan
1. Pitää olla joku optimoitava funktio (virhe funktio tai kustannusfunktio)
2. Arvataan optimoitava parametri
3. Lasketaan virhefunktion derivaatta arvatussa pisteessä
4. Säädetään arvattua optimoitavaa parametria lasketun derivaatan avulla
    - Säätöä varten derivaatan arvo kerrotaa (-1:llä) => säätö negat suuntaan
    - Säätöä voidaan kasvattaa tai pienentää oppimisnopeudella
    - Ja säätöhän on siis X = X - derivaatta*learningRate

'''

# f(x) = y = x^2 => f'(x) = 2x

x = np.linspace(-5,5,100)
y = np.power(x,2)

xa = 2
for i in range(10):
    learningRate = 1
    derivaatta = 2*xa
    xa = xa - derivaatta*learningRate
    ya = np.power(xa,2)

    plt.figure(1)
    plt.subplot(5,2,i+1),plt.plot(x,y),plt.plot(xa,ya,'r*')
plt.show()   