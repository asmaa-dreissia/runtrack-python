# affiche les instructionq 
def table_multi(N):
    for i in range (1,11):
        print(N,"*", i, "=", i*N)


# Demander à l'utilisateur de saisir un entier supérieur à zéro
while True :
     N = int(input("Saisir un nombre :"))
     if N > 0:
        break

# Appel de la fonction
table_multi(N)







