import pygame
from class_Button import Button
class Histoire:
    def __init__(self):
        #Largeur de l'écran
        self.width = 960
        #Hauteur de l'écran
        self.height = 568
        #Titre de l'écran
        pygame.display.set_caption("Crédit")
        #Appliquer la taille de l'écran à l'attribut screen
        #Les differentes police
        self.policeTitre = pygame.font.Font(None, 40)
        self.policeTitre.set_bold(True)
        self.policeTitre.set_underline(True)

        self.policeRoles = pygame.font.Font(None, 30)
        self.nbHistoire = 0
        self.policeSource = pygame.font.Font(None, 40)
        self.policeSource.set_underline(True)
        #Couleur du texte
        self.colorText = pygame.Color(255,255,255)
        #Liste des differents rolesw
        self.histoire1 = []
        self.histoire2 = []
        self.histoire3 = []
        #Listes des sources
        # self.TitreRole = self.policeTitre.render("Roles :",True,self.colorText)
        # self.TitreSource = self.policeTitre.render("Sources :",True,self.colorText)

        self.buttonNext = Button(650,10,"images/boutons/boutonPasser.gif")

        self.addRoles("Les meilleures solutions pour réduire la pollution et préserver notre planète les connais-tu ?",1)
        self.addRoles("Non ? Alors partons à l’aventure pour découvrir et en apprendreplus sur comment peut-on",1)
        self.addRoles("préserver le mieux notre planète. Ce périple te conduira à rencontrer des personnes qui te",1)
        self.addRoles("poserons des questions sur les effets et origines de toute cette pollution que que tu",1)
        self.addRoles("rencontreras. A toi de trouver les bonnes réponses, avancer dans ton périple et sauvez notre",1)
        self.addRoles("planète. C’est parti…",1)

        self.addRoles("Oh mais ? Que se passe-t-il ? Les nuages de pollution commencent à disparaitre ! Grâce à tes",2)
        self.addRoles("bonnes réponses tu réduis la pollution. Cela veut dire que tu as de bonnes pratiques et que",2)
        self.addRoles("tu sais ce qui est bon pour notre planète. Continu comme ça tu pourras bientôt réduire",2)
        self.addRoles("complètement la pollution.",2)

        self.addRoles("Bravo !! Tu as répondu avec succès à toutes les questions sur l’environnement. Tu es",3)
        self.addRoles("incollable sur l’écologie. Maintenant tu peux transmettre le message aux autres et tous",3)
        self.addRoles("ensemble nous pourrons sauvez notre planète.",3)


    def addRoles(self,histoire,num):
        text = histoire
        if num==1:
            self.histoire1.append(self.policeRoles.render(text,True,self.colorText))
        elif num==2:
            self.histoire2.append(self.policeRoles.render(text,True,self.colorText))
        else:
            self.histoire3.append(self.policeRoles.render(text,True,self.colorText))
    #fonction qui affiche les crédit
    def afficher(self,screen,num):
        screen.fill((0,0,0))
        screen.blit(self.buttonNext.image,(self.buttonNext.rect.x,self.buttonNext.rect.y))
        i = 80
        # screen.blit(self.TitreRole, (20,90))
        i += 40
        #I est la séparation entre 2 textes
        #Affiche tous les roles
        if num==1:
            for rolesCourant in self.histoire1:
                screen.blit(rolesCourant, (20,i+20))
                i+= 40
        elif num==2:
            for rolesCourant in self.histoire2:
                screen.blit(rolesCourant, (20,i+20))
                i+= 40
        else:
            for rolesCourant in self.histoire3:
                screen.blit(rolesCourant, (20,i+20))
                i+= 40
