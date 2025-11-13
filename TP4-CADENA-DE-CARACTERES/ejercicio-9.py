def longitud_palabras(cadena: str, v: str, n: str) -> tuple[str, int]:
    """
    Pre: cadena es una cadena de texto, v es la palabra vieja y n la palabra nueva a cambiar.
    Post: devuelve una lista de tuplas (palabra_limpia, largo) ordenadas por longitud.
    """
    # Intento, usando L. por comprension a medias
    # return ' '.join([letra for letra in cadena.split() if letra.isalpha()])
    palabras = cadena.split()
    signos = ".,;:!?¿¡()[]{}\"'"
    palabras_limpias = []
    for palabra in palabras:
        limpias = ''.join(letra for letra in palabra if letra not in signos)
        palabras_limpias.append((limpias, len(limpias)))
    ordenado = sorted(palabras_limpias, key=lambda x: x[1])

    return ordenado



def main():
    print(longitud_palabras("Hola, ¿como estas?", "", ""))


if __name__ == "__main__":
    main()
