# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

import unicodedata
import re

def normalizar_texto(texto: str) -> str:
    texto = unicodedata.normalize('NFKD', texto.lower()).encode('ASCII', 'ignore').decode('ASCII')
    return re.sub(r'[^a-z0-9]', '', texto)

def palabrainversa(palabra: str) -> str:
    return palabra[::-1]

def esPalindromo(palabra: str, palabra_inversa: str) -> bool:
    return palabra == palabra_inversa

if __name__ == "__main__":
    frase = input()
    frase_normalizada = normalizar_texto(frase)
    if esPalindromo(frase_normalizada, palabrainversa(frase_normalizada)):
        print(f"La frase '{frase}' es un palíndromo")
    else:
        print(f"La frase '{frase}' no es un palíndromo")