from Fonctions.ia import ia.*
#On creer le tableau (qui est une liste) qui sera la grille du morpion
Table = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# On Importe les éléments Besoin
#Initialisation des variables
Round = 1 #variable pour le tour
currentgame = 0
win = 1
stop = 1
draw = -1
game = currentgame
choix = 'X'

#Cette fonction détermine si une case est vide
def is_empty(x):
    if Table[x] == ' ':
        return True
    elif Table[x] == 'X' or Table[x]=='O':
        print("Veuillez Choisir un autre emplacement")

#Cette fonction affiche la grille vide
def AffichagePlateau():
    print("On est au Round", Round,"!")
    print(" %c | %c | %c " % (Table[0],Table[1],Table[2]))
    print("---|---|---")
    print(" %c | %c | %c " % (Table[3],Table[4],Table[5]))
    print("---|---|---")
    print(" %c | %c | %c " % (Table[6],Table[7],Table[8]))

#Cette fonction déterminer les conditions de victoire
def win():
    global game #indique qu'il s'agit de la même variable qu'à l'éxtérieur de la fonction
    if Table[0] == Table[1] == Table[2] != ' ' or Table[3] == Table[4] == Table[5] != ' ' or Table[6] == Table[7] == Table[8] != ' ' or Table[0] == Table[3] == Table[6] != ' ' or Table[1] == Table[4] == Table[7] != ' ' or Table[2] == Table[5] == Table[8] != ' ' or Table[0] == Table[4] == Table[8] != ' ' or Table[2] == Table[4] == Table[6] != ' ':
        game = win
    elif(Table[0] != ' ' and Table[1] != ' ' and Table[2] != ' ' and Table[3] != ' ' and Table[4] != ' ' and Table[5] != ' ' and Table[6] != ' ' and Table[7] != ' ' and Table[8] != ' '):
        game = draw  
    else:            
        game = currentgame

def PVP(Player1,Player2):
    global Round
    while game == currentgame:
        if Round == 1:
            AffichagePlateau()
        #Ce groupe de if permet d'alterner entre joueur1 et joueur2 
        if(Round % 2 != 0):    
            print("Joueur 1", Player1,"!")
            choix = 'X'
        else:
            print("Joueur 2", Player2,"!")
            choix = 'O'
        choice = int(input("Entre une position entre [0-8] : "))
        #Vérifie que l'emplacement est vide avant de remplir avec le choix du joueur
        if 0 <= choice <= 8:
            if is_empty(choice):
                Table[choice] = choix
                Round += 1
                win()
            AffichagePlateau()
        else:
            print("Veuillez Choisir un autre emplacement")
            choice = int(input("Entre une position entre [0-8] : "))
            if is_empty(choice):
                Table[choice] = choix
                Round += 1
                win()
            AffichagePlateau()
        if game == draw:
            print("Match Nul")
        elif game == win:
            Round -= 1    
            if(Round % 2 != 0):    
                print("Victoire", Player1, "\nFélicitation !!!")
            else:    
                print("Victoire", Player2, "\nFélicitation !!!")
def PVE():
    print("Ma grosse Bite")

    
print("Morpion\n")    
choixminijeu = int(input("Tapez 1 pour du PVP et 2 pour du PVE : "))

if choixminijeu == 1:
    Player1 = input("Entrez le nom du Joueur 1 : ")
    Player2 = input("Entrez le nom du Joueur 2 : ")
    PVP(Player1,Player2)
elif choixminijeu ==2:
    Player1 = input("Entrez le nom du Joueur 1 : ")
    PVE()


