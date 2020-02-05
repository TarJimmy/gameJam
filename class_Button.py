from class_Object import Object

class Button(Object):
    def __init__(self,x,y,cheminImage):
        super().__init__(x,y,cheminImage)

    def isClicked(self,pos):
        return self.rect.collidepoint(pos)
