class Animal:
    def __init__(self,name,espece,dodo):
        self.nom = name
        self.espece = espece
        self.sommeil = dodo
    def mange (self,poids,sommeil):
        poids += 10
        sommeil -= 10
        
    def dormir (self,poids,sommeil):
        poids -= 10
        sommeil += 10 
    def mort (self,poids,sommeil):
        if poids <= 0:
            print("the cat is dead again bruh")
        if sommeil <=0:
            print("the cat is dead again bruh")
        
class Chat(Animal):
    def __init__ (self,name,couleur):
        self.couleur = couleur
        
        Animal.__init__ (self)
        self.cri = "miaule"
        
    def
        
monChat = Chat("XxDarkHeadshotdu93xX")
input()