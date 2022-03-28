# Kevin Kuzu

class File:
    ''' classe File
    création d'une instance File avec une liste
    '''
    def __init__(self):
        ''' Initialisation d’une file vide'''
        self.contenu = []
    
    def estVide(self):
        "teste si la file est vide"
        return self.contenu==[]
    
    def defiler(self):
        '''défile et retourne la valeur défilée'''
        assert not self.estVide(),"File vide"
        return self.contenu.pop(0)
    
    def enfiler(self,x):
        "enfile"
        self.contenu.append(x)
    
    def taille(self):
        return len(self.contenu)
    
    def sommet(self):
        assert not self.estVide(),"File vide"
        return self.contenu[0]

    def __str__(self):
        return str(self.contenu)

if __name__=='__main__':
    F = File()
    for i in range(5):
        F.enfiler(i*2)
    print(F.contenu)
    a = F.defiler()
    print(F.contenu)
    print(a)
    print(F.taille())
    print(F.sommet())
    print(F)
    print(F.sommet())
    print(F.taille())