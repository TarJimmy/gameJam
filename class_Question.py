
class Question:
    def __init__(self):
        self.nomFichier = "questions.txt"
        self.textFichier = None
        self.numCourant = None
        self.question = None
        self.reponsesFausses = None
        self.reponseJuste = None
        self.solution = None
        self.recupTexteFichier()

    def recupTexteFichier(self):
        fichier = open(self.nomFichier, "r")
        self.textFichier = fichier.read()
        fichier.close()

    def recupQuestionNum(self,num):
        tab = self.textFichier.split('//')
        strNum = str(num)
        if num < len(tab):
            caseCourante=tab[num]
            #Vérification du numéro de la question supplémentaire
            if caseCourante[0] == strNum:
                tabInfo = caseCourante.split('|')
                self.question = tabInfo[1]
                i = 2
                for
            i += 1

        else:
            print("Erreur dans le nomre")

quest = Question()
rep = quest.recupQuestionNum()
print(rep)
