
class Question:
    def __init__(self):
        self.nomFichier = "questions.txt"
        self.textFichier = None
        self.numCourant = None
        self.question = None
        self.reponsesFausses = []
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
            caseCourante=tab[num-1]
            tabInfo = caseCourante.split('|')
            self.question = tabInfo[1]
            self.solution=tabInfo[len(tabInfo)-1]
            i = 2
            numSolution = tabInfo[len(tabInfo)-2]
            self.reponsesFausses.clear()
            while i < len(tabInfo)-2:
                reponse = tabInfo[i].split('-')
                if reponse[0]==numSolution:
                    self.reponseJuste = reponse[1]
                else:
                    self.reponsesFausses.append(reponse[1])
                    hey = 1
                i += 1
        else:
            print("Erreur dans le nombre")

quest = Question()
quest.recupQuestionNum(20)
quest.recupQuestionNum(10)
print(quest.question)
print(quest.reponsesFausses)
print(quest.reponseJuste)
print(quest.solution)
