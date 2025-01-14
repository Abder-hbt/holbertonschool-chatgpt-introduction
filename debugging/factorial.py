#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Diminue la valeur de n pour éviter une boucle infinie
    return result

if len(sys.argv) < 2:  # Vérifie qu'un argument a été fourni
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:  # Gère les cas où l'argument n'est pas un entier valide
    print("Please provide a valid integer.")
    sys.exit(1)
