'''
Lets make 2 classes Chef and ItalianChef. ItalianChef inherits from Chef
Note that one needs to pass self (about the same as this pointer in C++) to all
class functions including constructor.
'''

class Chef():             
    def __init__(self,nameOfTheChef):
        self.name = nameOfTheChef
    
    def printName(self):
        print(self.name)

    def makesalad(self):
        print(self.name,"is making salad")

    def makesoup(self):
        print(self.name,"is making soup")



class ItalianChef(Chef):
    def __init__(self,nameOfTheChef):
        self.name = nameOfTheChef

    def makepasta(self):
        print(self.name,"is making pasta")


    

chef1 = Chef("Gordon Ramsey")
chef1.printName()
chef1.makesalad()
chef1.makesoup()

chef2 = ItalianChef("Antony Bourdain")
chef2.makesoup()
chef2.makesalad()
chef2.makepasta()

