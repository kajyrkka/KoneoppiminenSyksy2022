import numpy as np
import matplotlib.pyplot as plt

'''
Kotitehtävän 2 videosta opittua:

1. perus plot komennot:
   x = np.arange(10)
   y = np.power(x,2)
   plt.title('neliöön korotus')
   plt.xlabel('aika')
   plt.ylabel('jannite')
   plt.grid() ei esitetty videossa, mutta kätevä.
   plt.plot(x,y,color='red',linewidth=5,linestyle='solid')
   plt.show() => tämä tarvitaan komentoriviltä suoritettuna, mutta ei näköjään jupyter notebookissa.

https://matplotlib.org/stable/tutorials/introductory/usage.html

1. Katsotaan kuvan elementit

2. Mitä eroa on object-oriented ja pyplot interface tyyleillä?

PYPLOT tyyli:
x = np.linspace(0, 2, 100)  # Sample data.
plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend();

OO-tyyli: => Minusta vähän hankalampi käyttää, mutta enemmän metodeja kuvan hallintaan.
x = np.linspace(0, 2, 100)  # Sample data.
# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend();  # Add a legend.

fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
xdata = np.arange(100)  # make an ordinal for this
data = 10**xdata
axs[0].plot(xdata, data)

axs[1].set_yscale('log')
axs[1].plot(xdata, data);

'''