class Pokemon:
    def init(self, nom, PV, force, resistance, type):
        self.__nom = nom
        self.__PV = PV
        self.__force = force
        self.__resistance = resistance
        self.__type = type
        
    def getName(self):
        print(self.__nom)
    def getForce(self):
        return self.__force
    def getResistance(self):
        return self.__resistance
    def getType(self):
        print(self.__type)
    def getPV(self):
        print(self.__PV)
    def setPV(self, PVPerdu):
        self.__PV = self.__PV - PVPerdu
        return self.__PV 

Bulbazar = Pokemon("bulbazar",20 , 8, 4, "plante")
Salah = Pokemon("Salah",18 , 10, 6, "feu")
Carat = Pokemon("Carat",24, 7, 3, "eau")

while (Bulbazar.getPV() > 0 and Salah .getPV() > 0):
    choix = int(input("Que doit faire Bulbazar : 1. Attaquer \n"))
    
    if (choix == 1):
        degats = Bulbazar.getForce() - Salah.getResistance()
        
        
 


