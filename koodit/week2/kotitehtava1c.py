from tehtava1 import signalAnalyser as S

Fs = 1000;

aika = int(input("Anna aika 1-10 sekunttia"))
print("Annoit ajaksi = ",aika, "sekunttia")

taajuus = int(input("Anna taajuus 0-500"))
print("Annoit taajuudeksi = ", taajuus)

lkm = int(input("Anna tulostettaien pisteiden lukumäärä"))
print("Tulostetaan", lkm, "kappaletta signaalipisteitä")

object = S(Fs,aika)
object.create(taajuus)
object.plot(0,lkm)
