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

        self.policeSource = pygame.font.Font(None, 40)
        self.policeSource.set_underline(True)
        #Couleur du texte
        self.colorText = pygame.Color(255,255,255)
        #Liste des differents rolesw
        self.mesRoles = []
        self.mesSources = []
        #Listes des sources
        # self.TitreRole = self.policeTitre.render("Roles :",True,self.colorText)
        # self.TitreSource = self.policeTitre.render("Sources :",True,self.colorText)

        self.buttonBack = Button(650,10,"images/boutons/boutonPasser.gif")

        self.addRoles("Les meilleures solutions pour réduire la pollution et préserver notre planète les connais-tu ?")
        self.addRoles("Non ? Alors partons à l’aventure pour découvrir et en apprendreplus sur comment peut-on")
        self.addRoles("préserver le mieux notre planète. Ce périple te conduira à rencontrer des personnes qui te" )
        self.addRoles("poserons des questions sur les effets et origines de toute cette pollution que que tu")
        self.addRoles("rencontreras. A toi de trouver les bonnes réponses, avancer dans ton périple et sauvez notre")
        self.addRoles("planète. C’est parti…")

        self.addRoles("Oh mais ? Que se passe-t-il ? Les nuages de pollution commencent à disparaitre ! Grâce à tes")
        self.addRoles("bonnes réponses tu réduis la pollution. Cela veut dire que tu as de bonnes pratiques et que")
        self.addRoles("tu sais ce qui est bon pour notre planète. Continu comme ça tu pourras bientôt réduire")
        self.addRoles("complètement la pollution.")

        self.addRoles("Bravo !! Tu as répondu avec succès à toutes les questions sur l’environnement. Tu es")
        self.addRoles("incollable sur l’écologie. Maintenant tu peux transmettre le message aux autres et tous")
        self.addRoles("ensemble nous pourrons sauvez notre planète.")


    def addRoles(self,histoire):
        text = histoire
        self.mesRoles.append(self.policeRoles.render(text,True,self.colorText))

    def addSource(self,element, source):
        text = element + " : " + source
        self.mesSources.append(self.policeSource.render(text,True,self.colorText))

    #fonction qui affiche les crédit
    def afficher(self,screen):
        screen.blit(self.buttonBack.image,(self.buttonBack.rect.x,self.buttonBack.rect.y))
        i = 80
        # screen.blit(self.TitreRole, (20,90))

        i += 40
        #I est la séparation entre 2 textes
        #Affiche tous les roles
        for rolesCourant in self.mesRoles:
            screen.blit(rolesCourant, (20,i+20))
            i+= 40
        #Affiche le titre des sources
        i += 20
        # screen.blit(self.TitreSource, (20,i+20))
        i += 40
        #affiche les sources
        for sourceCourantes in self.mesSources:
            screen.blit(sourceCourantes, (20,i+20))
            i+= 40
