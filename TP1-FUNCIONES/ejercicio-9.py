from typing import List, Tuple
import random

def cosecha(cantiada_naranjas: int) -> List[int]:
    """
    La funcion simulara el peso de cada naranja
    Pre: La cantidad de naranjas debe ser un numero entero positivo
    Post: La funcion debe devolver una lisa con el peso de cada naranja
    
    """
    peso = []
    for _ in range(cantiada_naranjas):
        peso.append(random.randint(150, 350))
    return peso

def clasificacion_naranjas(pesos: List[int]) -> Tuple[List[int], int]:
    """
    La funcion clasificara las naranjas que estan buenas o seran para jugo
    Pre: La funcion recibira la lista de paeso de las naranjas
    Post: Devolvera una lista con el peso de las naranjas buenas y la cantidad de naranjas para jugo
    """

    buenas = []
    jugo = 0
    for peso in pesos:
        if 200 <= peso <= 300:
            buenas.append(peso)
        else:
            jugo += 1
    return buenas, jugo

def cajones(naranjas_buenas: List[int]) -> Tuple[int, int]:
    """
    La funcion calculara la cantidad de cajones llenos y las naranjas que sobraron
    Pre: La funcion rebirira una lista con los pesos de las naranjas buenas
    Post: Retorna la cantidad de cajones y las naranjas que sobraron
    """

    en_cajones = len(naranjas_buenas)
    cajones = en_cajones // 100
    sobra = en_cajones % 100
    return cajones, sobra

def camiones(naranjas_buenas: List[int]) -> Tuple[int, int]:
    """
    La funcion calculara la cantiadad de camiones necesario para el transporte y tambien su estado util
    Pre: La funcion recibe una lista con los pesos de las naranjas buenas
    Post: Retorna la cantiadae de camiones y el peso del ultimo camión
    """
    total = sum(naranjas_buenas)
    capacidad_camion = 500000
    completos = total // capacidad_camion
    ultimo_camion = total % capacidad_camion

    return completos, ultimo_camion

def main():
    """ Funcion principal la cual coordina todas las operaciones"""
    try:
        cantidad_cosecha = int(input("Ingrese la cantiadad de naranjas que se cosecho: "))
        peso_naranjas = cosecha(cantidad_cosecha)
        buenas, jugo = clasificacion_naranjas(peso_naranjas)
        cajas, sobra = cajones(buenas)
        camion, ultimo_peso = camiones(buenas)

        print("--- RESULTADO DE LA COSECHA ---")
        print(f"Naranjas para jugo: {jugo} ")
        print(f"Naranjas buenas: {len(buenas)}")
        print(f"Cajones llenos: {cajas}")
        print(f"Naranjas sobrantes: {sobra}")

        print("--- TRANSPORTE ---")
        print(f"Se necesitan {camion} camiones completos")
        if ultimo_peso > 0:
            print(f"El ultimo camion tiene {ultimo_peso / 1000:.2f} Kg")
            if ultimo_peso >= 0.8 * 500000:
                print("El ultimo camion se despacha por cumplir con la ocupacion del 80%")
            else:
                print("El ultimo camion no sera despachado por no alcanzar el 80%")

        else:
            print("No hay peso para un nuevo camion")
    except ValueError:
        print("Deben ser numeros enteros validos")
if __name__ == "__main__":
    main()
        