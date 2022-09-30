import sklearn # This is anyway how package is imported
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

'''
1. Luetaan dataout.csv tiedosto pandas data frameksi siten, että tiedostosta luetaan vai
   sarakkeet x y z ja labels. Eli jätetään se indeksi sarake, joka koostuu 0,1,2 jonosta pois.
'''
df = pd.read_csv('dataoutTest.csv',
                  sep="\t",
                  #delimiter="\t",
                  #header=11,
                  #names=['ind', 'x', 'y', 'z' ,'suunnat'])
                  #header=0)
                  header=None)
                  #usecols=[1,2,3,4],
                  #names=['a','b','c','d'])

df = df.iloc[1:]
print(df.head())
#print(df['x'])  # eli näin pitäisi käsitellä, jos sarakkeilla on joku nimi, mutta kun poistetaan tuo eka rivi, niin sitten
                 # voidaan käsitellä sarakkeita numeroindeksein df[1] jne.
                 # ja sen eka rivin pystyi "nielaisemaan pois" df = df.iloc[1:] käskyllä eli indeksin arvosta 1 eteenpäin kaikki rivit mukaan.
#print(df['a'])
'''
Huomiot:

1. delimiter tai sep käy molemmat data erottimiksi

2. header = 11 tarkoittaa, että data aletaan lukemaan tiedoston yhdenneltätoista riviltä vasta. Ja tällöin sarakkeiden otsikoksi näyttää tulevan se edellinen 
   tiedoston rivi eli rivi 11. Ja jos sitten halutaan antaa paremmat nimet sarakkeille, niin se tehdään names=[] parametrilla
   Jos laittaa header = 0, niin siitä huolimatta dataframen alkuun tulee se x y z labels rivi ensimmäiseksi, koska se ei ole vielä dataa
   jos laittaa header = None, niin sitten enka riviksi ei enää tule x y z labels vaan sinne tulee ihan vain numeroindeksit.

3. CSV tiedostossa oli siis tuo ensimmäinen SARAKE = sarake 0, joka piti poistaa turhana. Ja se saatiin poistettua antamalla tuo usecols [1,2,3,4]
   eli ei käytetty col = 0:aa.
'''


