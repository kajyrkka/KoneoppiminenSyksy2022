import numpy as np

'''

Kotitehtävän2 ensimmäisestä videosta opittua:
1. Numpyn keskeinen dataelementti on N-dimensionaalinen array. Joka ensi silmäyksellä näyttää olevan
   ja toimivan samalla tavalla kuin Pythonin lista. Miksi siis toinen samanlainen datatyyppi? Siksi,
   että 1) Numpy array vie vähemmän muistia, 2) on paljon nopeampi kuin Python lista ja 3) on mukava
   käyttää (= ei tarvita toistorakenteita numpy arrayn läpikäymiseen) => Mistä nämä edut johtuvat??

2. Nähtiin uusi tapa tehdä for luuppi Pythonissa
   result = [(x+y for x,y in zip(l1,l2))] => kannattanee testata

Kotitehtävän2 toisesta videosta opittua:
1. a = np.array([1,2,3]) => yksi dimensionaalinen array
   a = np.array([[1,2,3],[4,5,6]]) => kaksi tai useampi dimensionaaliset näin
   a.ndim => kertoo arrayn dimensionaalisuude
   a.itemsize => kertoo yhden alkion viemien tavujen määrän
   a.dtype => kertoo datatyypin ja tämä voidaan antaa myös arrayn luonnissa parametrina (esim dtype = complex )
   a.size => elementtien lukumäärän
   a.respahe() => tällä voidaan muokata
   a.ravel() => tämä tekee monidimensionaalisesta yksidimensionaalisen. 
   a.shape => kertoo montako riviä ja montako saraketta (rivit, sarakkeet)
   a.min(), a.max(), a.sum(),a.sum(axis=0) => rivien summa, a.sum(axis=1) => sarakkeiden summa
   a.dot(b) => matriisikertolasku
   np.sqrt(a),np.std(a),
   np.zeros((shape tässä sulkujen sisällä))
   np.ones((2,4)) esimerkiksi
   np.arange(start,stop,step) Huomaa, että stop ei enää ole mukana
   np.linspace(start,stop,num) => esim np.linspace(1,5,100) luo 100 kappaletta arvoja tasaisesti 1:n ja 5:n välille. Nyt 5 on mukana.

Ja nämä on sitten siitä codebasics Numpy kirjaston listalta seuraavasta videosta, jonka nimi on
Numpy: slicing/stacking and indexing with boolean arrays

1. a = np.array([1,2,3,4])
   a[0:2] => palauttaa 1,2 eli EI arrayn kolmatta elementtiä
   a[-1] => palauttaa 4 eli arrayn viimeisen elementin => mitäs tulee jos a[-3:-1]?
   a[:] => valitsee kaikki alkiot:

   Tehtävä:
   a = np.arange(9)
   a = a.reshape(3,3) => Ota irti toinen rivi, alkio 9, sarakkeesta 2 ensimmäiset 2 riviä
                         kokeile alla olevat for luupit a arraylle
                         for row in a:
                            print(row)

                         for cell in a.flat:
                            print(cell)
   Stacking arrays:
   a = np.arange(6).reshape(3,2)
   b = np.arange(6).reshape(3,2)
   np.vstack((a,b)) => liittäminen pystysuorassa suunnassa
   np.hstack((a,b)) => liittäminen vaakasuorassa suunnassa
   np.hsplit(a,2) => jakaa arrayn kahdeksi vaakasuorassa suunnassa
   np.vsplit(a,2) => sama pystysuorassa suunnassa.

   Boolena indexing:
   a = np.arange(12).reshape(3,4)
   b = a > 6
   a[b] => eli valitsee a:sta ne elementit, jotka ovat suurempia kuin 6

'''
