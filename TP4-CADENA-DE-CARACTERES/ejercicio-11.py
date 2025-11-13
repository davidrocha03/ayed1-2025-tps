def contar_subcadena( cadena: str, sub_cadena: str):
    contador = 0
    i_sub = 0
    n_cadena = list(cadena.lower())
    for letra in n_cadena:
        if letra == sub_cadena[i_sub].lower():
            i_sub += 1
            if i_sub == len(sub_cadena):
                contador += 1
                i_sub = 0
    return contador
