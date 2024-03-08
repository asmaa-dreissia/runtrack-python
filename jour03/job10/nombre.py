def verefie(nombre):
    if type(nombre) != int or nombre < 0:
         print("Veuillez entrer un nombre entier positif")
         return
    
    if nombre % 2 == 0:
        print("le", nombre, "est un nombre paire")
    else:
          print("le", nombre, "est un nombre impaire")
 
# Test 
verefie(7)
verefie(5)
verefie(24)
verefie(9)
