from ej3_1_8 import *

def test_normalizar_texto():
    assert normalizar_texto("¡Anita lava la tina!") == "anitalavalatina"

def test_palabrainversa():
    assert palabrainversa("reconocer") == "reconocer"

def test_esPalindromo():
    frase = "Anita lava la tina"
    frase_normalizada = normalizar_texto(frase)
    assert esPalindromo(frase_normalizada, palabrainversa(frase_normalizada)) == True

def test_no_palindromo():
    frase = "Esto no es un palíndromo"
    frase_normalizada = normalizar_texto(frase)
    assert esPalindromo(frase_normalizada, palabrainversa(frase_normalizada)) == False

