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


data = np.zeros((len(df.index),4),dtype=int)              # Tehdään tilaa x, y, z ja vielä sille labelille, joka on muutettu numeroksi.
                                                # tämä siksi, että suodatus tapahtuu kätevästi myös tuon labelin osalta
data[:,0] = df[1].to_numpy()
data[:,1] = df[2].to_numpy()
data[:,2] = df[3].to_numpy()
data[:,3] = df[4].astype('category').cat.codes.to_numpy()    

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

x = suodatettu[:,0:3]                 # kiihtyvyysanturidata x,y,z
y = suodatettu[:,3]                   # tunnetut labeliti

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.3)
print(x_train.shape)
print(x_test.shape)

# Tehdään ensin random forests malli

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=2)
start = time.time()
model.fit(x_train,y_train)
print("Training random forest model took  =", (time.time()-start)*1000,"ms")
print("Random Forest mallin tarkkuus = ",model.score(x_test,y_test))

start = time.time()
print(model.predict(x_test))
print("Making predictions over whole test set took  =", (time.time()-start)*1000,"ms")

yPredicted = model.predict(x_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,yPredicted)
print("confusion matrix = ", cm)

'''
Huomiot:

1. Jos Pandasta osaa käyttää, niin on tehokas
2. Numpylläkin onnistuu ja kannattaisi ehkä ennemmin opetella Numpyn käyttö kunnolla.


'''


