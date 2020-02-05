import pygame

class Credit:
    def __init__(self,screen):
        pygame.init()
        #Largeur de l'écran
        self.width = 800
        #Hauteur de l'écran
        self.height = 800
        #Titre de l'écran
        pygame.display.set_caption("Crédit")
        #Appliquer la taille de l'écran à l'attribut screen
        self.screen = pygame.display.set_mode((self.width,self.height))

        #running est l'attribut ui précise si l'écran est activé
        self.running = False
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

    def addRoles(self,nom, roles):
        text = roles + " : " + nom
        self.mesRoles.append(self.policeRoles.render(text,True,self.colorText))

    def addSource(self,element, source):
        text = element + " : " + source
        self.mesSources.append(self.policeSource.render(text,True,self.colorText))

    #fonction qui affiche les crédit
    def afficher(self):


        #Met l'attribut d'affichage à True
        self.running = True
        #Affiche le titre des roles
        #I est la séparation entre 2 textes
        i = 40
        #Affiche tous les roles
        for rolesCourant in self.mesRoles:
            self.screen.blit(rolesCourant, (20,i+20))
            i+= 40
        #Affiche le titre des sources
        i += 20
        self.screen.blit(self.TitreSource, (20,i+20))
        i += 40
        print(self.mesSources)
        #affiche les sources
        for sourceCourantes in self.mesSources:
            self.screen.blit(sourceCourantes, (20,i+20))
            i+= 40
        #Tant qu'on continue à afficher la fenetre
        while self.running:
            #Met à jour l'écran


            ## Gérer les événements.
            # accueil.gerer_event()

            pygame.display.flip()

            #Parcours tous les évenements possibles
            for event in pygame.event.get():
                # si l'evenement est fermeture de fenetre
                if event.type == pygame.QUIT:
                    self.running = False
