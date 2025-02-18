# senha_logica.py

import random
import string

def gerar_senha(usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    caracteres = ""

    if usar_maiusculas:
        caracteres += string.ascii_uppercase

    if usar_minusculas:
        caracteres += string.ascii_lowercase

    if usar_numeros:
        caracteres += string.digits
        
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return None

    senha_gerada = ''.join(random.choices(caracteres, k=12))
    return senha_gerada

