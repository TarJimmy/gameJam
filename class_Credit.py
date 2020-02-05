import pygame
from class_Button import Button
class Credit:
    def __init__(self):
        #Largeur de l'écran
        self.width = 800
        #Hauteur de l'écran
        self.height = 800
        #Titre de l'écran
        pygame.display.set_caption("Crédit")
        #Appliquer la taille de l'écran à l'attribut screen
        #Les differentes police
        self.policeTitre = pygame.font.Font(None, 40)
        self.policeTitre.set_bold(True)
        self.policeTitre.set_underline(True)

        self.policeRoles = pygame.font.Font(None, 40)

        self.policeSource = pygame.font.Font(None, 40)
        self.policeSource.set_underline(True)
        #Couleur du texte
        self.colorText = pygame.Color(255,255,255)
        #Liste des differents rolesw
        self.mesRoles = []
        self.mesSources = []
        #Listes des sources
        self.TitreRole = self.policeTitre.render("Roles :",True,self.colorText)
        self.TitreSource = self.policeTitre.render("Sources :",True,self.colorText)

        self.buttonBack = Button(70,10,"images/boutons/boutonRetourAccueil.gif")

        self.addRoles("Saint-Laurent-Cyr Mark-Olivier", "Game Designer")
        self.addRoles("Jimmy Tardy", "Developpeur")
        self.addRoles("Cesar Watrin", "Developpeur")
        self.addRoles("Amine Benmansour", "Developpeur")
        self.addRoles("Lucas Zaetta", "Developpeur")

        self.addSource("exemple", "unesource.com")
        self.addSource("Exemple", "une deuxieme source.com")

    def addRoles(self,nom, roles):
        text = roles + " : " + nom
        self.mesRoles.append(self.policeRoles.render(text,True,self.colorText))

    def addSource(self,element, source):
        text = element + " : " + source
        self.mesSources.append(self.policeSource.render(text,True,self.colorText))

    #fonction qui affiche les crédit
    def afficher(self,screen):
        screen.blit(self.buttonBack.image,(self.buttonBack.rect.x,self.buttonBack.rect.y))
        i = 80
        screen.blit(self.TitreRole, (20,90))

        i += 40
        #I est la séparation entre 2 textes
        #Affiche tous les roles
        for rolesCourant in self.mesRoles:
            screen.blit(rolesCourant, (20,i+20))
            i+= 40
        #Affiche le titre des sources
        i += 20
        screen.blit(self.TitreSource, (20,i+20))
        i += 40
        #affiche les sources
        for sourceCourantes in self.mesSources:
            screen.blit(sourceCourantes, (20,i+20))
            i+= 40
