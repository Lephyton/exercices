class Personne :

    def __init__(self, prenom, nom, age, sexe, argent, objet):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.sexe = sexe
        self.argent =  argent
        self.objet = ["mangues", "tomates", "conconbres", "oignons"]
        print("Bonjour", prenom, "comment vas tu  ? ")

    
    def get_age(self):
        return self.age
    def get_prenom(self):
        return self.prenom
    def get_nom(self):
        return self.nom
    def get_sexe(self):
        return self.sexe
    def get_argent():
        return self.argent
    def get_objet():
        return self.objet

    def presentation(self):
        print("bonjour tout le monde mon est :", self.prenom, self.nom, "j'ai :", self.age, "et je suis un(e)", self.sexe)

    def veillir(self, v):
        self.age += v
        print("he bien:", v,"an déjà !!!" )
    
    def travailler(self, m):
        self.argent += m
        print("grace à mon travaille je gagne :", m ,"en plus,je possède desormais", self.argent )
    
    
        
tob = Personne("Thomas", "TOB", 23, "Homme", 1000, ["mangues"])
tob.veillir(1)
tob.presentation()
tob.travailler(50)
virginie = Personne("Virginie", "MATANGO", 18, "Femme", 100, ["mangues"])
virginie.veillir(1)
virginie.presentation()

podol = Personne("Podol", "MBOCK", 73, "Homme", 450, ["mangues"])
podol.veillir(1)
podol.presentation()
