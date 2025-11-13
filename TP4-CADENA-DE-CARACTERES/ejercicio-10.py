def reemplazar_palabras(cadena: str, v: str, n: str):
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
    pass

if __name__ == "__main__":
    pass
