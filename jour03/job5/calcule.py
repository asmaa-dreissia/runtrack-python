# Fonction nommée « calcule » 

def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        return num1 / num2
    if operator == '%':    
        return num1 % num2
    
# Test
print("la somme des deux nombres est de", (calcule(5, '+', 3)) )
print("le produit de deux nombres est de", (calcule(10, '*', 2)) )
