
class Parametre:
    def __init__(self):
        #pour affichage correct sur vidéo-projecteur
        self.widthMax = 960
        self.heightMax = 568

        self.difficulte = 1

    def verifWidth(self,width):
        if (width < self.widthMax):
            return width
        else:
            print("Largeur de la fenetre redimensionnée")
            return widthMax

    def verifHeight(self,height):
        if (height < self.heightMax):
            return height
        else:
            print("Hauteur de la fenetre redimensionnée")
            return heightMax
