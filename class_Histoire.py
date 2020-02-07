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
        self.policeGameOver = pygame.font.Font(None, 90)
        self.policeGameOver.set_bold(True)
        #Couleur du texte
        self.colorText = pygame.Color(255,255,255)
        self.colorGameOver = pygame.Color(255,0,0)
        #Liste des differents rolesw
        self.histoire1 = []
        self.histoire2 = []
        self.histoire3 = []
        self.histoire4 = []

        self.titreGameOver = self.policeGameOver.render("Game Over",True,self.colorGameOver)
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

        self.addRoles("Bravo !! Tu as répondu avec succès à toutes les questions sur l’environnement. Tu es",3)
        self.addRoles("incollable sur l’écologie. Maintenant tu peux transmettre le message aux autres et tous",3)
        self.addRoles("ensemble nous pourrons sauvez notre planète.",3)

        self.addRoles("Vous n'avez plus d'oxygène, vous êtes donc mort.",4)
        self.addRoles("Vous pouvez toujours vous entrainer afin de devenir incollable sur l'écologie !",4)

    def addRoles(self,histoire,num):
        text = histoire
        if num==1:
            self.histoire1.append(self.policeRoles.render(text,True,self.colorText))
        elif num==2:
            self.histoire2.append(self.policeRoles.render(text,True,self.colorText))
        elif num==3:
            self.histoire3.append(self.policeRoles.render(text,True,self.colorText))
        elif num==4:
            self.histoire4.append(self.policeRoles.render(text,True,self.colorText))
    #fonction qui affiche les crédit
    def afficher(self,screen,num, player = None):
        screen.fill((0,0,0))
        screen.blit(self.buttonNext.image,(self.buttonNext.rect.x,self.buttonNext.rect.y))
        i = 120
        # screen.blit(self.TitreRole, (20,90))
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
        elif num ==3:
            for rolesCourant in self.histoire3:
                screen.blit(rolesCourant, (20,i+20))
                i+= 40

            text = "Vous avez obtenue : " + str(round(player.oxygene)) + "points d'oxygènes"
            screen.blit(self.policeTitre.render(text,True,self.colorText))
        elif num ==4:
            screen.blit(self.titreGameOver,(300, 200))
            i += 200
            for rolesCourant in self.histoire4:
                screen.blit(rolesCourant, (20,i+20))
                i+= 40
