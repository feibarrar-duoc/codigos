def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========\n1. Agregar paciente\n2. Buscar paciente\n3. Eliminar paciente\n4. Actualizar estado\n5. Mostrar pacientes\n6. Salir\n=====================================\n")
def leer_opcion():
    try:
        while True:
            opcion = int(input("Ingrese una opción: "))
            if 1<= opcion <= 6:
                return opcion
                break
            else:
                print("La opción ingresada no existe\n")
    except:
        print("La opción ingresada debe ser un número")
        
def validar_nombre():
    while True:
        nombre = input("Ingrese nombre del paciente: ")
        espacio = ""
        if nombre != espacio:
            print("Nombre ingresado con éxito")
            return nombre
            break
        else:
            print("El nombre no puede estar vacío")

def validar_edad():
    try:
        while True:
            edad = int(input("Ingrese la edad del paciente: "))
            if edad >= 1:
                print("Edad ingresada con éxito")
                return edad
                break
            else:
                print("La edad debe ser mayor a 0")
    except:
        print("La edad debe ser un número")

def validar_temp():
    try:
        while True:
            temp = float(input("Ingrese la temperatura: "))
            if 35.0 <= temp <= 42.0:
                print("Temperatura ingresada con éxito")
                return temp
            else:
                print("La temperatura debe estar entre 35.0 y 42.0")
    except:
        print("La temperatura debe ser un número")
        
        