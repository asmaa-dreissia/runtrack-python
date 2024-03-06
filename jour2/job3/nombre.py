# Créez un programme qui affiche dans le terminal tous les nombres de 0 à 100 compris SAUF 26, 37, 88.

for nombre in range (101):
 if nombre not in [26, 37, 88]:
    print(nombre)


#[]défini une liste en Python. 
#for pour parcourir tous les nombres de 0 à 100 inclus. 
#not in vérifie si un élément n'est pas présent dans une séquence 
