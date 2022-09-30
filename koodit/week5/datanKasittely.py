import sklearn # This is anyway how package is imported
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

df = pd.read_csv('dataoutTest.csv',
                  sep="\t",
                  header=None,                 # lukee tiedoston ekarivin joka on tekstiä dataan mukaan
                  usecols=[1,2,3,4])           # valitaan vain sarakkeet 1-4
df = df[1:]                                    # poistetaan eka rivi dataframesta

'''
dfcopy = df.copy()
#df = df[ df[1].astype(int) < 1024 ]            # eli dataframesta valitaan rivit joilla ehto toteutuu
df = df[ (df[1].astype(int) < 1024) & (df[2].astype(int) < 1024) & (df[3].astype(int) < 1024) ]  
                                                # eli jätetään rivi, jos kaikki x, y ja z arvot pienempiä kuin 1024
#dfcopy = dfcopy [dfcopy[1].astype(int) >= 1024]
dfcopy = dfcopy [(dfcopy[1].astype(int) >= 1024) | (dfcopy[2].astype(int) >= 1024) | (dfcopy[3].astype(int) >= 1024)]
                                                # eli suodatetaan jos x, y tai z arvo suurempi kuin 1024
print("suodatuksen jälkeen jäljellä", len(df.index))
print("poistettiin seuraava rivit",dfcopy)
'''
# vai olisiko helpompaa siirtyä heti tiedostosta luvun jälkeen numpyn käyttöön?

print("riveja = ",len(df.index))
data = np.zeros((len(df.index),4),dtype=int)              # Tehdään tilaa x, y, z ja vielä sille labelille, joka on muutettu numeroksi.
                                                # tämä siksi, että suodatus tapahtuu kätevästi myös tuon labelin osalta
data[:,0] = df[1].to_numpy()
data[:,1] = df[2].to_numpy()
data[:,2] = df[3].to_numpy()
data[:,3] = df[4].astype('category').cat.codes.to_numpy()    

print("numpy array = ", data[50:])

#tehdään suodatin
suodatin = np.zeros((len(df.index),4),dtype=bool) 
for i in range(len(df.index)):
    if( (data[i,0]<1024) & (data[i,1]<1024) & (data[i,2]<1024) ):
        suodatin[i,:] = [True,True,True,True]
    else:
        suodatin[i,:] = [False,False,False,False]

suodatettu = data[suodatin]
riveja = int(len(suodatettu)/4)
suodatettu = suodatettu.reshape(riveja,4)

print("suodatin = ", suodatin[50:])
print("suodatettu = ",suodatettu[40:])





'''
Huomiot:

1. Jos Pandasta osaa käyttää, niin on tehokas
2. Numpylläkin onnistuu ja kannattaisi ehkä ennemmin opetella Numpyn käyttö kunnolla.


'''


