#Manejo de string

name:str

name = "mAria"

name_transformed = name.lower().capitalize()

print(name_transformed)


#Funcion para ver ubicación de memoria de una var

print(f"{id(name)}+{id(name_transformed)}")


"""
?# Python tiene incorporado el unicode (texto universal)

List -> [], mutables
tuples -> (), inmutables
dictionaries -> {:} mutables
set -> {} inmutables


?# Estructuras de control

if - simple

elif
"""

if name == "mAria":
    print("hola")
elif name != "maria":
    print("nao")

"""
//////////////////////////////////////////////////////////////////////////////
"""

categoria_A = 4500;
categoria_B = 5999;
categoria_C = 9488;

cat_paciente = int(input("Indique una categoria del paciente:\n 1: Categoria A \n 2: Categoria B\n 3: Categoria C\nEscriba 4 para salir "))
init = int(input("Escribe 1 si quieres comenzar, 0 para salir"))

while init == 1:
    if cat_paciente == 1:
        print(f"Cobro paciente: {categoria_A}")
    
    elif categoria_B == 2:
        print(f"Cobro paciente: {categoria_B}")
    
    elif categoria_C == 3:
        print(f"Cobro pacient: {categoria_C}")
    
    init = int(input("Escribe 1 si quieres seguir registrando pacientes, 0 para salir"))


"""
!# Tarea
"""