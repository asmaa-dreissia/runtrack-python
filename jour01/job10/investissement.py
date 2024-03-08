# Montant initial de l’investissement
montant_initial = float(input("montant initial de l'investissemnt:"))

# Taux de rendement annuel en pourcentage
taux_rendement = float(input("valeur du taux de rendement annuel en pourcentage:"))

# gain annuel
gain_annuel= montant_initial * (taux_rendement / 100)
print("le gain annuel est de", gain_annuel)


# capital augmenté de 5000 € et le taux de 2%
montant_initial += 5000
taux_rendement += 2

# nouveau gain de l’investisseur
nvx_gain = montant_initial * (taux_rendement / 100)
print("le nouveau gain de l'investisseur est de",nvx_gain)

# retrait de 10% du montant total, rendement diminue de 1%.

