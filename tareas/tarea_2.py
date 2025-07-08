#Tarea #2

id_usuario = ""
nombre_usuario = ""
apellido_usuario = ""
tipo_consulta = ""
valor_a_pagar = ""

bandera = int(input("Bienvenido a nuestro sistema de salud! Escribe 1 para abrir el menú y 0 para salir: "))


menu = """
¿Qué quieres hacer?
1. Ingresar mis datos
2. Consultar mis datos
0. Salir
"""


while True:
    if bandera == 1:
        print(menu)
        opcion_usuario = int(input("Ingresa tu opción: "))

        if opcion_usuario == 1:
            id_usuario = input("Ingrese su ID: ")
            nombre_usuario = input("Ingrese su nombre: ")
            apellido_usuario = input("Ingrese su apellido: ")
            tipo_consulta = input("Tipo de consulta: ")
            valor_a_pagar = input("Valor a pagar: ")
            print("Datos guardados exitosamente!")
            
        elif opcion_usuario == 2:
            if id_usuario == "":
                print("No hay datos ingresados. Por favor, ingrese sus datos primero.")
            else:
                print(f"ID: {id_usuario}")
                print(f"Nombre: {nombre_usuario} {apellido_usuario}")
                print(f"Tipo de consulta: {tipo_consulta}")
                print(f"Valor a pagar: {valor_a_pagar}")
                
        elif opcion_usuario == 0:
            print("Gracias, hasta luego.")
            break
            
        bandera = int(input("\n¿Desea continuar? (1 = Sí, 0 = No): "))
        
    elif bandera == 0:
        print("Gracias, hasta luego.")
        break



