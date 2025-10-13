def cargar_usuarios() -> list[tuple[int, int]]:
    """
    La funcion se encargara de cargar y validar los datos ingresados por el usuario
    Pre: Tiene pre-condiciones las cuales se tienen que validar
        Datos:
            - El numero afiliado debe tener un rango de 4 digitos enteros positivos. Rango 1000 a 9999
            - El motivo de reserva debe ser (0-Caso de urgencia), (1-En caso de tuno)   
            - Para finaliar la carga de datos debe ser de ingresando -1
    Post: La funcion retorna una lista con los datos cargados.
    """

    pacientes = []

    while True:
        while True:
            afiliado = int(input("Ingrese su numero afiliado (-1 Para salir): "))
            if afiliado == -1:
                return pacientes
            if afiliado < 1000 or afiliado > 9999:
                print("Fuera del rango permitido. Vuelva a intentarlo")
            else:
                break
        while True:
            print("--- TIPOS DE TURNO DISPONIBLE ---")
            print("0 -> Turno por urgencia")
            print("1 -> Turno general")
            turno = int(input("Ingrese el tipo de turno: "))
            if turno < 0 or turno > 1:
                print("Tipo de turno no disponible. Vuelva a intentarlo")
            else:
                break
        pacientes.append((afiliado, turno))
        print("Carga exitosa")

def mostrar_listado(lista: list[tuple]) -> list[tuple  ]:
    """
    La funcion se encarga de mostrar un listado de los pacientes por urgencia y por turno
    Segun el orden de llegada

    Pre: La funcion utiliza como parametro una lista de los pacientes cargados
    Post: Retorna una lista con pacientes por turno y una lista con pacientes 
    por turno con urgencia
    """
    urg = []
    norm = []
    for a, b in lista:
        if b == 0 :
            urg.append((a, b))
        elif b == 1:
            norm.append((a, b))
    return urg, norm

def num_afiliado(busqueda: int, lista: list[tuple]) -> tuple[int, int]:
    """
    La funcion mostrara cuantas veces un afiliado asistio por TURNO y por URGENCIA

    Pre: Como parámetro recibe una lista de tuplas con los pacientes cargados y el
    el Numero de afiliado a buscar 
    Post: Retorna una tupla de enteros la cual se refiere cuantas fueron las veces por
    TURNO y por TURNO POR URGENCIA
    """
    por_Urg = 0
    por_Tur = 0
    encontrado = False

    for busq_afiliado , turno in lista:
        if busq_afiliado == busqueda:
            encontrado = True
            if turno == 0:
                por_Urg += 1
            elif turno == 1:
                por_Tur += 1
    
    if encontrado:
        return por_Tur, por_Urg
    else:
        return None



if __name__ == "__main__":

    registro = cargar_usuarios()
    print(registro)
    urgencia, turno = mostrar_listado(registro)
    print("-"*20)
    print(f"Pacientes por Urgencia: {urgencia}")
    print(f"Pacientes por Turno: {turno}")
    print("-"*20)
    while True:
        while True:
            afil_busq = int(input("Ingresa el Num Afiliado a informar: "))
            if afil_busq == -1:
                print("Saliendo")
                break
            if afil_busq < 1000 or afil_busq > 9999:
                print("Rango no permitido. Vuelva a intentarlo")
            elif afil_busq == '':
                print("No se admiten espacios vacios. Vuelva a intentarlo  ") 
            else:
                urg, tur = num_afiliado(afil_busq, registro)
                print(f"Afiliado {afil_busq} por URGENCIA: {urg} TURNO GENERAL: {tur}")

                    
