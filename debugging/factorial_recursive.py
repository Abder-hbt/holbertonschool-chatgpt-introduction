#!/usr/bin/python3
import sys

# Description:
# La fonction factorial calcule le factoriel d'un nombre entier n de manière récursive.

# Paramètres:
# n (int): un entier pour lequel on souhaite calculer le factoriel.

# Retour:
# La fonction retourne un entier qui est le factoriel de n.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Vérification si un argument est passé en ligne de commande
if len(sys.argv) != 2:
    print("Usage: python3 factorial.py <number>")
    sys.exit(1)

try:
    # Convertir l'argument en entier
    number = int(sys.argv[1])
    
    if number < 0:
        print("Le nombre doit être un entier positif ou nul.")
        sys.exit(1)

    # Calculer le factoriel
    f = factorial(number)
    print(f)

except ValueError:
    print("Veuillez entrer un nombre entier valide.")
    sys.exit(1)
