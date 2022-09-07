'''
Luo lista, tuple, set ja dictionary muuttujat
Laita jokaiseen kolme elementtiä ja tulosta keskimmäinen
print komennolla
'''

lista = [1, "Second element", (1,2)]
print("This way we take second element",lista[1], "as lista starts from element 0")
for i in range(3):  # 0,1,2 for i in range(2,15,3)
    print(lista[i])

tuplee = (1,"TUPLE ELEMENT", (1,2,3))
print("This way we take second element",tuplee[1], "as lista starts from element 0")
for i in range(3):
    print(tuplee[i])

setti = {1,"huuhaa",2,(1,2,3)}

print(setti)

sanakirja = {"kariKoti":"0505119222","kariTyö":"0401415096","jokuMuu":"1234456"}
print("Karin kotinumero =", sanakirja.get("kariKoti"))
print("Karin työnumero =", sanakirja.get("kariTyö"))
print("Sanakirjastakin on hankalaa ottaa toinen alkio",sanakirja["kariTyö"])
print(sanakirja.get("kariTyö"))
print(sanakirja.items())