def nombre_mes(n: int):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", 
    "Junio","Julio", "Agosto", "Septiembre", "Octubre",
     "Noviembre", "Diciembre"]

    try:
        return meses[n-1]
    except IndexError:
        print("Indice no encontrado")
        return ""

def main():
    while True:
        n = input("Ingrese num (Enter para salir): ")
        if n == "":
            break
        try:
            num = int(n)
            print(nombre_mes(num))
        except ValueError:
            print("Tipo de dato no valido")

if __name__ == "__main__":
    main()


    