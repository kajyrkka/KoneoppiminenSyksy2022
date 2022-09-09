import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
Pandas videosta kuultua:
1. Data science = data analytics on suuren datamäärän analysointia siten,
   että datasta pyritään saamaan vastauksia tiettyihin kysymyksiin. Esim.
   minä päivänä covid-19 tautiin sairastuneiden lukumäärä sairaalassa
   kasvoi kaikista eniten.

2. Excel on yksi työkalu, jolla data analytiikkaa voidaan tehdä, mutta
   excel ei ole hyvä jos dataa on suuri määrä ja excelistä ei välttämättä
   löydy kaikkia analytiikkatyökaluja. Toinen vaihtoehto olisi käyttää 
   pelkkää Python ohjelmointikieltä, mutta silloin joutuu tekemään paljon
   omaa koodia esim excel tai jonkun muun muotoisen tiedoston lukemiseksi
   ja erilaisten analyysityökalujen koodaamiseksi ja testaamiseksi. Pandas
   kirjasto on videon mukaan helppo käyttöinen ja sieltä löytyy kaikki
   tarvittava erilaisten analyysien tekemiseksi.

Videon Pandas esimerkeistä opittuja asioita:
df['columnName'].max() => hakee maksimiarvon dataframen columnName sarakkeesta
df['columnName'].mean() => laskee keskiarvon ja samaan tyyliin löytyy paljon muita
                           funktioita joilla voi käsitellä yhden (tai useamman) sarakkeen
                           dataa




Oman koodin kanssa värkätessä opittuja asioita:
1. Jos yrittää lukea dataframe read_csv() funktiolla käyttäen web-osoitetta,
   niin saattaapi tulla virheilmoitus HTTP Error 403: Forbidden. Tämä
   johtunee Web-serverin security asetuksista, jotka kieltävät python clientin
   tekemän pyynnön. Tähän on monia kiertoratkaisuja, mutta ei tapella niiden 
   kanssa tällä kurssilla käytetään Web-browseria siihen, että haetaan tiedosto
   sillä ja talletetaan samaan hakemistoon Pandas koodin kanssa.

2. Jos jostain syystä pelkkä df = read_csv('tiedostonimi.csv') ei toimi, vaikka
   tiedosto on varmasti samassa hakemistossa kuin Pandas koodikin, niin silloin
   polun tiedostoon joutuu antamaan muodossa df = read_csv(c\\)
   df = read_csv('C:\\KoneoppiminenSyksy2022\\koodit\\week2\\national-history.csv')
   df = read_csv('C:/KoneoppiminenSyksy2022/koodit/week2/national-history.csv')

3. Miksi videossa dataframen saattoi printata taulukoksi vain df -komennolla ja
   VisualStudio codessa joutuu sanomaan print(df)? Ehkä siksi, että videolla kaveri
   ei käytä VisualStudio Codea vaan jupyter notebook sovellusta..

4. Kokeilin tehdän oman excel tiedoston ja lukea sen 
   df = pd.read_excel('modulattori.xlsx') -komennolla
   => Ei toiminut ennenkuin asensi virtual environmenttiin
   pip install openpyxl
   modulin.
'''


df = pd.read_excel('modulattori.xlsx',header = None,           
                   names=['t','data','carrier','mod','demod'],
                   usecols=[0,1,2,3,4],
                   skiprows=[0])
#print(df)
print("carrier sarakkeen max arvo = ",df['carrier'].max())
print("carrier sarakkeen min arvo = ",df['carrier'].min())
print("carrier sarakkeen keskiarvo arvo = ",df['carrier'].mean())
print(df['carrier'].dtype)
count = (df['carrier'] == 1).sum()
print('Count of ones in Column  Carrier   : ', count)


t = df['t'].to_numpy()
dat = df['data'].to_numpy()
mod = df['mod'].to_numpy()
dem = df['demod'].to_numpy()

plt.figure(1)
plt.subplot(2,2,1)
plt.plot(t,mod)
plt.title('moduloitu')
plt.subplot(2,2,2)
plt.plot(t,dem)
plt.title('demoduloitu')

plt.subplot(2,2,3)
plt.plot(df['t'],df['mod'])
plt.title('moduloitu')
plt.subplot(2,2,4)
plt.plot(df['t'],df['demod'])
plt.title('demoduloitu')
plt.show()
'''

""" 
Tehtävä 1: 
-asenna Pandas kirjasto virtual environmenttiisi ellet ole jo asentanut (pip install pandas)
-lataa https://covidtracking.com/data/download/national-history.csv tiedosto käsiteltäväksi


"""

df=pd.read_csv('C:\\Users\\kajyrkka\\PythonSW\\KoneoppiminenSyksy2022\\koodit\\week2\\national-history.csv',
               header=0,
               names=['date','deaths','hospitalInc','hospitalNow'],
               usecols=[0,1,5,6])



dates = df['date'].to_numpy()
dead = df['deaths'].to_numpy()
Hinc = df['hospitalInc'].to_numpy()
Hnow = df['hospitalNow'].to_numpy()

plt.figure(1)
plt.subplot(3,1,1)
plt.plot(dead)
plt.title('Deaths')

plt.subplot(3,1,2)
plt.plot(Hinc)
plt.title('Hospitalized Increased')

plt.subplot(3,1,3)
plt.plot(Hnow)
plt.title('Hospitalized Currently')

plt.figure(2)
plt.subplot(3,1,1)
plt.plot(np.flip(dead))
#plt.plot(dead[::-1])
plt.title('Deaths')

plt.subplot(3,1,2)
plt.plot(np.flip(Hinc))
#plt.plot(Hinc[::-1])
plt.title('Hospitalized Increased')

plt.subplot(3,1,3)
plt.plot(Hnow[::-1])
plt.title('Hospitalized Currently')


plt.show()

maksimi = Hinc.max()
indeksi = np.where(Hinc == maksimi)

print("maksimi päiväkohtainen kasvu = ", maksimi)
print("Ja tuo maksimi löytyy kohdasta = ", indeksi)
print("Ja tuo tapahtui päivämäärällä", dates[indeksi])

print("Saman voi tehdä myös suoraan dataFramen avulla seuraavasti")
print("maksimi arvo = ",df['hospitalInc'].max())
print("Ja tuon maksimin paikka = ",df[df['hospitalInc']==df['hospitalInc'].max()].index)
paikka = df[df['hospitalInc']==df['hospitalInc'].max()].index
print("ja tuo tapahtui päivämäärällä = ", df['date'][paikka])

print("Hnow shape = ", Hnow.shape)
print("Hnow dtype = ", Hnow.dtype)
'''