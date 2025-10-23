def carga_socios() -> list[tuple[int]]:
    """
    La funcion se encarga de la carga de los socios

    Pre: 
        -EL numero de socio debe ser de 5 digitos positivos
        -Para cancelar la carga de datos debe ingresar 0
    Post:
        - Retorta una lista de tuplas con los numeros de socios ingresados
    """
    socios = []
    while True:
        try:
            num_socio = int(input("Ingresa numero de socio (0 Para salir): "))
            if num_socio == 0:
                if not socios:
                    return "Se cancelo la carga de socios"
                else:   
                    print("Carga Exitosa")
                    return socios 
            if num_socio < 10000 or num_socio > 99999:
                print("Valor fuera del rango. Vuelva a intentarlo")
            else:
                socios.append((num_socio,))
        except ValueError:
                print("Entrada invalida. Vuelva a intentarlo.")

def info_socio(lista: list[tuple]) -> dict[int,int]:
    """
    La funcion informa la cantidad de veces que ingreso un socio en particular  
    
    Pre: El socio a buscar debe ser un entero de 5 digitos y la lista debe estar cargada 
    Post: Retorna como entero las veces que ingreso
    """
    conteo = {}
    for actual in lista:
        if actual in conteo:
            conteo[actual] += 1
        else:
            conteo[actual] = 1
    print("--- Informe socios ---")
    for num, valor in conteo.items():
        print(f"Socio: {num[0]} Veces: {valor}")
    return "Resultado exitoso"

if __name__ == "__main__":        
    carga = carga_socios()
    print(carga)
    b = info_socio(carga)
    print(b)   

