class Personne():
    def __init__(self, nom, prenom, age, ville) -> None:
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.ville = ville

    def vieillir(self,annees):
        self.age=self.age+annees
        print(f'{self.prenom} a vielli de {annees} ans, il est agé de {self.age} ans')




perso1 = Personne("Cantaloub", "Jerome", 41, "St-naz")
perso2 = Personne("Yan", "Bertand", 46,"St-naz")

perso1.vieillir(20)
perso2.vieillir(5)