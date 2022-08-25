# KoneoppiminenSyksy2022

Kukin opiskelija tekee oman github repositoryn, jonne tallentaa omat
kurssin aikana tekemänsä Python koodit. Opettaja näyttää esimerkin 
1) miten repository tehdään Githubiin
2) miten se kloonataan omalle koneelle haluttuun hakemistoon
3) miten tuohon hakemistoon asennetaan pythonin virtual environment
4) miten .gitignore tiedostolla vältetään venv tiedostojen siityminen githubiin
5) miten lokaalilla koneella tehdyt muutokset siirretään githubiin

Ja edelliset tehdään siksi, että seuraavan periodin projektissa
kukin opiskelija pitää omia koodejaan omassa Github repositoryssä eli
nyt jo totutellaan git bash käyttöön ja githubin kanssa toimimiseen.

Yksityiskohtaiset ohjeet kohtien 1-5 toteuttamiseksi:


Asennetaan Python 3.10 (https://www.python.org/downloads/) ja git (https://git-scm.com/downloads) ellei ole jo asennettu

Tehdään tunnukset githubiin ja kirjaudutaan sisään. Tehdään githubiin oma repository KoneoppiminenSyksy2022, joka 
kloonataan omalle koneelle siihen hakemistoon, missä halutaan pitää kurssin Python ohjelmia.
	
Koneoppiminen hakemistoon asennetaan python -m virtualenv koodit -komennolla pythonin virtual environment

Koneoppiminen hakemistoon lisätään .gitignore tiedosto ja sinne rivit (jotta Python asennusta ei kopioida githubiin, 
vain koodit hakemisto ja sen sisällä olevat python koodit)

koodit/Lib
koodit/Scripts
koodit/.gitignore
koodit/pyvenv.cfg

Ja sitten git add . , git commit -m "Python virtual environment for koneoppiminen", git push origin main -komennot. 
		
Ja jos koodit hakemistoa ei näy git status komennosta huolimatta, niin pakota git tunnistamaan koodit hakemisto tekemällä 
sinne tehtava1.py tiedosto ja antamalla git add -f koodit/tehtava1.py -komento ja sen jälkeen sitten taas commit ja push komennot.
