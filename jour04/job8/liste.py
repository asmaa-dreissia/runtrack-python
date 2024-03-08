#Écrire un programme qui calcule la somme de toutes les valeurs paires 
liste = L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
nbrpaire = 0

for number in L:
    if number %2 == 0:
        nbrpaire += number

print("la somme des nombres paire dans la liste est de", nbrpaire)
      