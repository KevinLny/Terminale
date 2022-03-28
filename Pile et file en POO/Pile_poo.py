#Kevin Kuzu

class Pile:
    ''' classe Pile : création d'une instance Pile avec
    une liste Python '''
    def __init__(self):
        "Initialisation d'une pile vide"
        self.contenu=[]

    def estVide(self):
        "teste si la pile est vide"
        return self.contenu==[]
    
    def depiler(self):
        "dépile et renvoie la valeur dépilée"
        assert not self.estVide(),"Pile vide"
        return self.contenu.pop()
    
    def empiler(self,x):
        "empile"
        self.contenu.append(x)
    
    def taille(self):
        c = self
        compteur = 0
        while not c.estVide():
            c.depiler()
            compteur += 1
        return compteur

    def sommet(self):
        c = self
        x = c.contenu.pop(0)
        return x
    
    def __str__(self):
        return self.contenu

if __name__ == "__main__":
    p=Pile()
    for i in range(5):
        p.empiler(2*i)
    a=p.depiler()
    print(a)
    print(p.contenu)
    print(p.estVide())
    print(p.contenu)
    print(p.taille)
    print(p.sommet())