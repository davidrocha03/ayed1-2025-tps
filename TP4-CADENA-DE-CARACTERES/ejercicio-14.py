def leer_correo_electronico(correo: str) -> bool:
    """
    Pre: correo debe ser una cadena de texto.
    Post: Devuelve True si el correo es válido, False en caso contrario.
          Un correo es válido si:
          - Contiene exactamente un '@'
          - El usuario solo contiene caracteres alfanuméricos
          - El dominio termina en '.com' o '.com.ar' y tiene al menos un caracter antes del punto
    """
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
    """
    Pre: no recibe parametros
    Post: Permite ingresar correos electrónicos hasta que el usuario presione Enter.
          Imprime los dominios únicos válidos ingresados, ordenados alfabéticamente.
    """
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
    for i in sorted(validos):
        print(i)


if __name__ == "__main__":
    main()
