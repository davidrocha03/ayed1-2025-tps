def reemplazar_palabras(cadena: str, v: str, n: str):
    """
    Pre: 'cadena' es una cadena; 'v' y 'n' son cadenas a comparar y reemplazar.
    Post: devuelve una tupla (cadena_modificada, cantidad_reemplazos).
    """
    palabras = cadena.split()
    contador = 0
    nueva = []
    for palabra in palabras:
        if palabra == v:
            palabra = n
            contador += 1
        nueva.append(palabra)
    return ' '.join(nueva), contador


def main():
    print(reemplazar_palabras("hola mundo hola", "hola", "chau"))


if __name__ == "__main__":
    main()
