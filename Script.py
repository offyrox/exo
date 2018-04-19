def exo01():

    a = "Je dois faire des sauvegardes réguliere de mes fichiers."
    print(a * 500)




def exo02():

    a = 1

    while a < 1000:
        print(a)
        a = a + 2


def exo03():

    a = 0
    b = 13

    while a < 11:
        print(a * b)
        a = a + 1

def exo04():

    a = input("Un mot svp")
    print(len(a))

def exo05():
    a = input("Un nombre entier svp")
    if(a % 2)== 0:
        print("Votre nombre est Pair")
    else:
        print("Votre numero est impair")

def exo06():

    a = (int)
    a = input("nombre entre 10 et 20 :  ")
    if(int( a ) > int(20)):
        print("trop grand")
        exo06()
    if(int( a ) < int(10)):
        print("trop petit")
        exo06()
    else:
        print("beau boulot")

def exo07():

    a = (int)
    a = input("un nombre svp :  ")
    c = (int)
    c = 0
    while (int(10) > int(c)):
        c = c + int(1)
        b = int( a ) + int( c )

        print( b )

def exo08():

    a = 0
    b = (int)
    b = input("entrez un nombre :  ")

    while a < 11:
        print(a * int(b))
        a = a + 1



def exo09():

    a = (int)
    a = input("un nombre stp : ")
    b = (int)
    b = 0
    c = (int)
    c = 0
    while(int( a ) > int( b )):
        b = b + int(1)
        c = c + b
    else:
        print( c )

def exo10():

    a = (int)
    a = input("Age :  ")
    if(int(a) < int(6)):
        print("Tu n'est rien")
    if(int(a) == 6 or int(a) == 7):
        print("Poussin")
    if(int(a) == 8 or int(a) == 9):
        print("Pupille")
    if(int(a) == 11 or int(a) == 10 ):
        print("Minime")
    if(int(a) == 12 or int(a) > int(12)):
        print("Cadet")


def exo11():
    a = (int)
    a = input("nombre de produit  : ")
    b = (int)
    b = input("Prix unitaire d'un produit HT : ")
    c = int(a) * int(b)
    e = (int(c) + (0.20 * int(c)))





    print("Nombres d'article :" )
    print( a )
    print("Prix HT(1 article) :" )
    print( b )
    print("Prix HT(tout les article) : " )
    print( c )
    print("Prix TTC :" )
    print( e )

