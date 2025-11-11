class ceroMayorError(Exception):
    pass
def datos_invalidos(n: int)-> None:
    try:
        num= input("ingrese numero: ")
        if num > 0:
            raise ceroMayorError()
    except ceroMayorError as e:
        print("El numero debe ser mayor a cero") 
    except ValueError:
        pritn("Debe ingresar un numero entero")
    except:
        print("Error desconocido")
    finally:
        return num
