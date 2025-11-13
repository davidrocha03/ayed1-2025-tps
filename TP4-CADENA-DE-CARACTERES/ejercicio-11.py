def contar_subcadena(cadena: str, sub_cadena: str) -> int:
    """
    Pre: 'cadena' y 'sub_cadena' son cadenas de texto.
    Post: devuelve la cantidad de veces que 'sub_cadena' aparece dentro de 'cadena', ignorando mayúsculas/minúsculas.
    """
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


def main():
    print(contar_subcadena("Hola hola HoLa", "hola"))


if __name__ == "__main__":
    main()
