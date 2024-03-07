def time_to_text(minute):
    heures = minute // 60  # divise le nombre total de minutes par 60 pour donner le nombre d'heures dans le nombre total de minutes.
    minutes_restantes = minute % 60 # permet de trouver le nombre de minutes restantes après avoir converti les heures.

    print(heures," heures et", minutes_restantes, "minute")

# Test
time_to_text (68)
time_to_text (400)
time_to_text (20)