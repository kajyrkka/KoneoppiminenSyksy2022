import numpy as np
import matplotlib.pyplot as plt
'''
Let's look in to matplotlib library properties and train ourselves
with Numpy array manipulations. Your tasks are the following:
1) Make 256*256 pixel picture (instructions given below). Current
   example plots RGB picture where Red component is all ones and G,B components are zero
   thus picture is all red. Your task is to modify picture in such a way that pixels
   at range 0-127 (rows), 0-127 (columns) show red picture area
   at range 0-127 (rows), 128-256 (columns) show green picture area
   at range 128-256 (row), 0-127 (columns) show blue picture area
   at range 128-256 (row), 128-256 (columns) show gray picture area 

'''
'''
size = 256
kuva = np.zeros((size,size,3))
#kuva[:,:,0]= np.ones((size,size))
kuva[128:,128:,0:] = 0.5*np.ones((128,128,3))
plt.imshow(kuva)
plt.show()
'''
'''
Let's look at matplotlib library basic usage tutorials. There is an example
how to create 3 figures as shown below

fig1 = plt.figure()  # an empty figure with no Axes
fig2, ax = plt.subplots()  # a figure with a single Axes
fig3, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

Your tasks are the following:
1) create 4 NumPy arrays containing 1 second sine signals with 1, 2, 3, 4 Hz
    HINT:
    create first time t = np.arange(0,1,0.01), where t starts from 0, ends at 0.99
    and then use np.sin and np.pi functions to genereate certain sine signals with certain
    frequencies. And remember the equation = sin(2*pi*f*t)
2) print 1 Hz sine signal to fig1
3) print 2 Hz sine signal to fig2
4) print 1,2,3,4 Hz sine signals to fig3 subplots. HINT: remember that axs is 2*2 matrix. 
   thus accessing second subplot goes with axs[0,1], where 0 = first row, 1 = second column.
5) print titles to all 3 figures
6) change line type and color of line of all 4 subplots at fig3 

7) And finally as we hopefully saw during the lectures that one can put
   many signals to a matrix and then just print matrix and all columns are
   seen as separate signals. Make signal matrix where you have a 1 second 2 Hz sine
   signal and its second power. And print those to a same figure.

'''

Fs = 1000
Ts = 1/Fs
t = np.arange(0,1,Ts)
s1 = np.cos(2*np.pi*1*t)
s2 = np.sin(2*np.pi*2*t)
s3 = np.abs(s2)
s4 = np.abs(s1)
S = np.zeros((t.size,2))
S[:,0] = s3
S[:,1] = s4

plt.figure(1)
plt.subplots_adjust(hspace=1)
plt.subplot(3,1,1),plt.plot(s1),plt.title("1 Hz kosini signaali")
plt.subplot(3,1,2),plt.plot(s2),plt.title("2 Hz sini signaali")
plt.subplot(3,1,3),plt.plot(S),plt.title("Itseisarvot molemmista signaaleista")
plt.show()
'''
#plt.figure(2)
fig2,ax = plt.subplots(3,1,figsize=(5,7))
w = None
vSpace = 1
hSpace = 2
plt.subplots_adjust(left=w,bottom=w,right=w,top=w,wspace=vSpace,hspace=hSpace)
ax[0].plot(s1),ax[0].set_title("1 Hz kosini signaali")
ax[1].plot(s2),ax[1].set_title("2 Hz sini signaali")
ax[2].plot(S),ax[2].set_title("Itseisarvot molemmista signaaleista")
plt.show()
'''