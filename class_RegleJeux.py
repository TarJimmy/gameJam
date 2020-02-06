import pygame
from class_Button import Button
class RegleJeux:
    def __init__(self):
        self.height = 568
        self.width = 960
        self.bg = pygame.image.load("images/backgrounds/bg6.jpg").convert()
        self.clavier = pygame.image.load("images/boutons/clavierPetit.jpg")
        self.fleche= pygame.image.load("images/boutons/flechePetit.jpg")
        self.gardien= pygame.image.load("images/joueur/L11E.png")
        self.oxygene=pygame.image.load("images/objects/oxygenePetit.png")
        self.policeRegle = pygame.font.Font(None,35)
        self.policetexte = pygame.font.Font(None,22)
        self.policecommande= pygame.font.Font(None,18)
        self.texte0= self.policeRegle.render('Règles du jeu',True,(96,76,141))
        self.texte1 = self.policetexte.render('Objectif :',True,(255,0,0))
        self.texte2= self.policetexte.render('Durant la partie vous devez traverser la ville,',True,(255,255,255))
        self.texte3= self.policetexte.render("polluée, à l'aide de ventilateurs. Votre objectif",True,(255,255,255))
        self.texte4= self.policetexte.render('est de répondre correctement aux questions du gardient',True,(255,255,255))
        self.texte5= self.policetexte.render('de la nature. Ce personnage est essentiel dans la partie.',True,(255,255,255))
        self.texte6= self.policetexte.render("Il permet de vous transmettre de l'oxygène pour avancer.",True,(255,255,255))
        self.texte7= self.policetexte.render("À chaque ville le gardien vous pose une question.",True,(255,255,255))
        self.texte8= self.policetexte.render('Si vous trouvez la réponse il vous transmet une bonbonne',True,(255,255,255))
        self.texte9= self.policetexte.render("d'oxygène nécessaire pour votre survie.",True,(255,255,255))
        self.texte10= self.policetexte.render('Vous devrez faire preuve de vigilance car votre oxygène diminue',True,(255,255,255))
        self.texte11= self.policetexte.render('progressivement à cause de vos actions. Vous devez allier dextérité',True,(255,255,255))
        self.texte111=self.policetexte.render("et bon sens afin d'atteindre la dernière ville.",True,(255,255,255))
        self.texte12=self.policetexte.render('Dans le cas contraire vous mourrez asphyxié.',True,(255,255,255))
        self.texteBonus1=self.policetexte.render("Les bombonnes d'air que vous trouverez sur votre chemin",True,(255,255,255))
        self.texteBonus2=self.policetexte.render("permettent de récupérer de l'oxygène facilement.",True,(255,255,255))
        self.texte121=self.policetexte.render('Bonne chance !',True,(255,255,255))

        self.texte13= self.policetexte.render('Commandes :',True,(255,0,0))
        self.texte14= self.policecommande.render("La touche ESPACE permet d'activer les ventilateurs",True,(255,255,255))
        self.texte15=self.policecommande.render("afin de vous propulser vers le haut.",True,(255,255,255))
        self.texte16=self.policecommande.render('Les flèches directionelles permettent de déplacer le joueur',True,(255,255,255))
        self.texte17=self.policecommande.render('à gauche et à droite pour traverser les villes.',True,(255,255,255))


        self.texte18=self.policecommande.render('Le gardien de la nature vous pose des questions. Si vous ',True,(255,255,255))
        self.texte19=self.policecommande.render("répondez juste il vous donne de l'oxygène. Dans le cas",True,(255,255,255))
        self.texte20=self.policecommande.render('contraire il vous en retire. Des bombonnes sont également',True,(255,255,255))
        self.texte21=self.policecommande.render("disponibles et donnent accès des bonus d'oxygène.",True,(255,255,255))
        self.buttonBack = Button(160,510,"images/boutons/boutonRetourAccueil.gif")

    def afficher(self,surface):
        pygame.display.set_caption("Règles du jeux")
        surface.blit(self.bg,(0,0))
        # pygame.display.flip()
        surface.blit(self.buttonBack.image,(self.buttonBack.rect.x,self.buttonBack.rect.y))
        surface.blit(self.clavier,(660,120))
        surface.blit(self.fleche,(680,230))
        surface.blit(self.gardien,(690,390))
        surface.blit(self.oxygene,(760,400))

        surface.blit(self.texte0,(400,10))
        surface.blit(self.texte1,(170,60))
        surface.blit(self.texte2,(40,100))
        surface.blit(self.texte3,(40,130))
        surface.blit(self.texte4,(40,160))
        surface.blit(self.texte5,(40,190))
        surface.blit(self.texte6,(40,220))
        surface.blit(self.texte7,(40,250))
        surface.blit(self.texte8,(40,280))
        surface.blit(self.texte9,(40,310))
        surface.blit(self.texte10,(40,340))
        surface.blit(self.texte11,(40,370))
        surface.blit(self.texte111,(40,400))
        surface.blit(self.texte12,(40,430))
        surface.blit(self.texteBonus1,(40,460))
        surface.blit(self.texteBonus2,(40,490))
        # surface.blit(self.texte121,(40,510))
        surface.blit(self.texte13,(700,60))
        surface.blit(self.texte14,(580,190))
        surface.blit(self.texte15,(580,205))
        surface.blit(self.texte16,(580,360))
        surface.blit(self.texte17,(580,375))
        surface.blit(self.texte18,(580,448))
        surface.blit(self.texte19,(580,461))
        surface.blit(self.texte20,(580,475))
        surface.blit(self.texte21,(580,489))
        pygame.display.update()
