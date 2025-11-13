import random as rn

def encuenta_numero() -> int:
    """
    Pre: no recibe parametros
    Post: Juega con el usuario a adivinar un número generado aleatoriamente entre 1 y 500.
          Devuelve la cantidad de intentos realizados hasta adivinar correctamente.
          Maneja errores de ingreso no numérico.
    """
    x: int = rn.randint(1, 500)
    c: int = 0
    print("--ADIVINA EL NUMERO--")
    
    while True:
        try:
            n: int = int(input("Ingrese Num: "))
            c += 1
            if n < x: 
                print(f"{n} es menor")
            elif n > x:
                print(f"{n} es mayor")
            else:
                print("Correcto")
                return c
        except ValueError:
            print("Ocurrió un error")
            c += 1

def main() -> None:
    """
    Pre: no recibe parametros
    Post: Ejecuta el juego de adivinar número y muestra la cantidad total de intentos.
    """
    i: int = encuenta_numero()
    print(f"En total se intentaron {i} veces")    

if __name__ == "__main__":
    main()

