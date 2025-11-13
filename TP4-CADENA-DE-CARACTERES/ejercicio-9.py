def longitud_palabras(cadena: str, v: str, n: str) -> tuple[str, int]:
    # Intento, usando L. por comprension a medias
    # return ' '.join([letra for letra in cadena.split() if letra.isalpha()])

    palabras = cadena.split()
    signos = ".,;:!?¿¡()[]{}\"'"
    palabras_limpias = []
    for palabra in palabras:
        limpias = ''.join(letra for letra in palabra if letra not in signos)
        palabras_limpias.append(limpias, len(limpias))
    ordenado = sorted(palabras_limpias, key= lambda x: x[1])
        

def main():
    pass

if __name__ == "__main__":
    pass    


