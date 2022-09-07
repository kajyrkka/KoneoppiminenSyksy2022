import numpy as np

'''
1. Miten täytetään numpy array datalla?
2. Tuliko tehtyä yksiuloitteinen vektori vai matriisi? Miten vaakavektorista pysty
3. Miten yksittäisiä alkioita otetaan "irti" numpy vektorista tai matriisista?
4. Operaatiot vektoreilla vaativat samaa shapea ja samaa kokoa.
5. Peruskomentoja, jotka pitää hanskata:
    np.arange
    np.linspace
    np.reshape
    vektori = np.array([1,2,3]) => print("vektorin shape = ",vektori.shape) 
'''

a = np.array([[1,2,3],[4,5,6]]) # => Hankalaa!
print("vektori a = ",a," ja vektorin shape = ",a.shape,a.dtype)

b = np.arange(1,7,1)
b = b.reshape((3,2))
print("vektori b = ",a," ja vektorin shape = ",b.shape,b.dtype)

c = np.random.randn(10)
d = np.ones(10)
print("c*d on helppo jos molemmat yhtä pitkiä ja saman suuntaisia vektoreita =", c*d)

print("shape d = ", d.shape)
