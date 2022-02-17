#Agenda de teléfonos en python

def mostrarMenu():
    opc = 0
    while (opc < 1 or opc > 6):
        print("1- Añadir contacto")
        print("2- Borrar contacto")
        print("3- Editar contacto")
        print("4- Buscar contacto")
        print("5- Mostrar todos los contactos")
        print("6- Salir")
        try:   
            opc = (int) (input("Seleccione una opción: "))
        except:
            print("Tienes que introducir un número entre 1 y 6. Vuelve a intentarlo")
            opc=0
        if (opc < 1 or opc > 6):
            print("********* Opción no válida ************")
    return opc


