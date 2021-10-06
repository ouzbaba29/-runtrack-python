class laby():
    def __init__(self, rows, cols):
        self.nb_ligne = rows  # n
        self.nb_colonne = cols  # m
        self.mat_horiz = [[True for colonne in range(self.nb_colonne)] for ligne in range(self.nb_ligne + 1)]
        self.mat_vert = [[True for colonne in range(self.nb_colonne + 1)] for ligne in range(self.nb_ligne)]

    def __str__(self):

        """retourner une chaine de caracère contenant la grille de jeu"""

        resultat = ""
        mur_horiz = "+---"
        non_mur_horiz = "+   "
        mur_vert = "|   "
        non_mur_vert = "    "
        fin_mur_vert = "|"

        for ligne in range(self.nb_ligne):
            # begin
            for colonne in range(self.nb_colonne):
                "affiche des murs horizontaux"
                if self.mat_horiz[ligne][colonne] == True:
                    resultat += mur_horiz
                else:
                    resultat += non_mur_horiz

            resultat += "+\n"

            for colonne in range(self.nb_colonne + 1):
                "affiche des murs verticaux"
                if self.mat_vert[ligne][colonne - 1] == True:
                    resultat += mur_vert
                elif self.mat_vert[ligne][colonne] == True:
                    resultat += fin_mur_vert
                else:
                    resultat += non_mur_vert

            resultat += "\n"

        for colonne in range(self.nb_colonne):
            if self.mat_horiz[ligne][colonne] == True:
                resultat += mur_horiz
            else:
                resultat += non_mur_horiz

        resultat += "+\n"

        return (resultat)

        # end


##class explo_exhau():
##
##    def __init__(self,cell):
##    self.cell= [[False for colonne in range(self.nb_colonne)] for ligne in range(self.nb_ligne)]
##
##    def __str__(self):
##
##    #var
##
##    N=False
##    S=False
##    E=False
##    O=False
##
##    ouest : colonne-1
##    est:colonne+1
##    nord : ligne +1
##    sud : ligne-1
##
##    p=[[ligne],[colonne]]
##    p.append () "ajoute un élément à la pile"
##    p.pow ()    "enlève un élément à la pile"


def main():
    # var
    nb_ligne = ""
    nb_colonne = ""

    # begin

    while True:
        nb_ligne = input("Veuillez entrer un nombre entier de ligne pour le labytrinthe : ")
        nb_colonne = input("Veuillez entrer un nombre entier de colonne pour le labyrinthe : ")

        nb_ligne = int(nb_ligne)
        nb_colonne = int(nb_colonne)

        l = laby(nb_ligne, nb_colonne)
        print(l)
        break

    # end


# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()