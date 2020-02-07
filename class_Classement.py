import pygame
from class_Button import Button
class Classement:
    def __init__(self):
        #Largeur de l'écran
        self.width = 960
        #Hauteur de l'écran
        self.height = 568
        #Titre de l'écran
        pygame.display.set_caption("Classement")
        #Appliquer la taille de l'écran à l'attribut screen
        #Les differentes police
        self.policeTitre = pygame.font.Font(None, 40)
        self.policeTitre.set_bold(True)
        self.policeTitre.set_underline(True)
        self.policeRoles = pygame.font.Font(None, 30)
        self.nbHistoire = 0
        self.policeSource = pygame.font.Font(None, 40)
        self.policeSource.set_underline(True)
        self.policeGameOver = pygame.font.Font(None, 90)
        self.policeGameOver.set_bold(True)
        #Couleur du texte
        self.colorText = pygame.Color(255,255,255)
        self.colorGameOver = pygame.Color(255,0,0)
        self.titre = self.policeTitre.render("Game Over",True,self.colorText)
        #Liste des differents rolesw
        fichier = open("records.txt","r")
        self.text = fichier.read()
        fichier.close()
        self.tab = self.text.split("//")
        self.buttonBack = Button(160,510,"images/boutons/boutonRetourAccueil.gif")

    #fonction qui affiche les crédit
    def afficher(self,screen):
        screen.fill((0,0,0))
        screen.blit(self.buttonBack.image,(self.buttonBack.rect.x,self.buttonBack.rect.y))
        i = 80
        screen.blit(self.titre,(60,i+20))
        i+=60
        fichier = open("records.txt","r")
        tout = fichier.read()
        record = 0
        tout = tout.split('//')
        if(len(self.tab)>0):
            for recordCourant in self.tab:
                coupRecord = recordCourant.split("--")
                date = coupRecord[len(coupRecord)-2].split(" ")
                text = coupRecord[len(coupRecord)-1] + " oxygènes: " + date[len(date)-2] + " à " + date[len(date)-1]
                pText = self.policeRoles.render(text,True,self.colorText)
                screen.blit(pText,(60, i+20))
                i+= 40
        else:
            pText = self.policeRoles.render("Pas de record enregistré",True,self.colorText)
            screen.blit(pText,(60, i+20))
