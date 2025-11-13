def nombre_mes(n: int) -> str:
    """
    Pre: n debe ser un número entero que represente un mes (1-12)
    Post: Devuelve el nombre del mes correspondiente a n. 
          Devuelve cadena vacía si n no corresponde a ningún mes.
    """
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
             "Junio", "Julio", "Agosto", "Septiembre",
             "Octubre", "Noviembre", "Diciembre"]

    try:
        return meses[n - 1]
    except IndexError:
        print("Error: número de mes fuera de rango")
        return ""


def main():
    while True:
        n = input("Ingrese número de mes (Enter para salir): ")
        if n == "":
            break
        try:
            num = int(n)
        except ValueError:
            print("Error: debe ingresar un número entero")
            continue
        mes = nombre_mes(num)
        if mes:
            print(f"El mes es: {mes}")


if __name__ == "__main__":
    main()


    