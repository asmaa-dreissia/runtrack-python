L = [8, 24, 48, 2, 16]
multiples3 = 0

for number in L:
    if number % 3 == 0:
        multiples3 += 1       #compte le nombre de multiples de 3 dans la liste. Chaque fois qu'un multiple de 3 est trouvé, le compteur est augmenté de 1.

print("Le nombre de multiples de 3 dans la liste est de :", multiples3)