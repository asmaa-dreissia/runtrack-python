# variable représentant le produit
nom = ("ordinateur")
prix_unitaire = 430
qtt_stock= 23

print("Produit:", nom)
print("Prix unitaire:",prix_unitaire,"euro")
print("Nombre en stock:", qtt_stock)

# Ajout des produits en stock. 

quantite_ajoutee = int(input("Entrez la quantité de produits à ajouter en stock: "))
qtt_stock += quantite_ajoutee

print("Après ajout de stock :")
print("Produit:", nom)
print("Prix unitaire:", prix_unitaire, "euro")
print("Nombre en stock:", qtt_stock)

# inflation de 10%

inflation = 10
prix_unitaire *= (1 + inflation / 100)

print("mise à jour du prix avec l'inflation de 10% :")
print("Produit:", nom)
print("Prix unitaire:", prix_unitaire, "euro")
print("Nombre en stock:", qtt_stock)