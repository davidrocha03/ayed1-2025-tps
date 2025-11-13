class ceroMayorError(Exception):
    pass
def datos_invalidos()-> None:
    while True:
        try: 
            num = int(input("Ingresa numero: "))
            if num < 0:
                raise ceroMayorError("El numero debe ser mayor a cero")
            return num
        except ceroMayorError as e:
           print(e) 
        except ValueError:
            print("Debe ingresar un numero entero")
        except:
            print("Error desconocido")
            

def main():
    print(datos_invalidos())

if __name__ == "__main__":
    main()