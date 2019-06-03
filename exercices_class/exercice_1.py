class Personne :

    def __init__(self, prenom, nom, age, sexe):
        self.prenom = prenom
        self.nom = nom
        self.age = age
        self.sexe = sexe
        print("Bonjour", prenom, "comment vas tu  ? ")

    
    def get_age(self):
        return self.age
    def get_prenom(self):
        return self.prenom
    def get_nom(self):
        return self.nom
    def get_sexe(self):
        return self.sexe

    def presentation(self):
        print("bonjour tout le monde mon est :", self.prenom, self.nom, "j'ai :", self.age, "et je suis un(e)", self.sexe)

    def veillir(self, v):
        self.age += v
        print("he bien:", v,"an déjà !!!" )
    
    
        
tob = Personne("Thomas", "TOB", 23, "Homme")
tob.veillir(1)
tob.presentation()

virginie = Personne("Virginie", "MATANGO", 18, "Femme")
virginie.veillir(1)
virginie.presentation()

podol = Personne("Podol", "MBOCK", 73, "Homme")
podol.veillir(1)
podol.presentation()
