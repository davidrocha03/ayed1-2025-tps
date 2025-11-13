def leer_correo_electronico(correo: str):
    p = correo.split()
    if correo.count("@") != 1:
        return False
    usuario, dominio = correo.split("@")
    if not usuario.isalnum():
        return False

    if not (dominio.endswith(".com") or dominio.endswith(".com.ar")):
        return False

    if len(dominio.split(".")[0]) < 1:
        return False
    return True

def main():
    #validos = []
    validos = set()
    while True:
        correo = input("Ingrese correo (enter para salir): ")
        if correo == "":
            break
        if leer_correo_electronico(correo):
            dominio = correo.split("@")[1].lower()
            validos.add(dominio)
        else:
            print("Correo invalido")
    #for i in sorted(set(validos))
    for i in sorted(validos):
        print(i)

if __name__ == "__main__":
    main()
