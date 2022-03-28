class Voiture:
    def __init__(self, marque, modele, couleur) -> None:
        self.marque = marque
        self.modele = modele
        self.couleur = couleur

    def klaxonner(self):
        print(f'tut tut !!')
    
    def accelerer(self):
        print(f'vroooom !!')

voiture1 = Voiture("Renault", "Kangoo", "Blanche")
voiture2 = Voiture("Peugot", "5008", "Noire")

voiture1.couleur = "jaune"
voiture1.klaxonner()

voiture2.couleur = "jaune"
voiture2.accelerer()