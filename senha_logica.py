import random
import string

def gerar_senha():
    caracteres = ""

    if usar_maiusculas.get():
        caracteres += string.ascii_uppercase

    if usar_minusculas.get():
        caracteres += string.ascii_lowercase

    if usar_numeros.get():
        caracteres += string.digits
        
    if usar_simbolos.get():
        caracteres += string.punctuation
