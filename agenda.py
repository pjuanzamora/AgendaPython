#Agenda de teléfonos en python

#Muestra el menú con las opciones y devuelve la opción
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

#Mostrar todos los contactos de la agenda
def mostrarTodos(vAgenda):
    for contacto in vAgenda:
        print(contacto)

#Añadir un contacto a la agenda con el formato nombre-telefono en una lista
def addcontact(vAgenda):
    print("Guardando contacto")
    nombre = input("Dime el nombre del contacto: ")
    tel = input("Dime el telefono del contacto: ")
    contacto = nombre+"-"+tel
    vAgenda.append(contacto)



print("*******  AGENDA DE TELÉFONOS TIC2 *********")
vAgenda = []
opc = mostrarMenu()
while (opc != 6):
    if (opc==1):
        addcontact(vAgenda)
        print("Opcion 1")
    elif (opc==2):
        print("Opcion 2")
    elif (opc==3):
        print("Opcion 3")
    elif (opc==4):
        print("Opcion 4")
    else:
        print("Contactos guardados:")
        mostrarTodos(vAgenda)

    opc = mostrarMenu()
   
print("Saliendo de la agenda... Encriptando datos por seguridad")
    
    
