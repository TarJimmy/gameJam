import random
from class_Object import Object

class Oxygene(Object):
    def __init__(self,x,y,cheminImage = "images/objects/oxygene.png"):
        super().__init__(x,y,cheminImage)
        bonus = random.randint(10, 30)
        self.redimensionne(80,65)
