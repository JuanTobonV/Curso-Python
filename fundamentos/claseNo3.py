"""
 Tipos de datos

 - Las listas son mutables 
 - Aceptan diferentes tipos de datos 
 - Tienen metodos que permiten manipularlas
 - Son iterables

"""


customer = [7912212, "Pepito", "Perez", 152000.23, True]

#Para acceder a un dato

print(customer[3])

#Para agregar un nuevo elemento(al final)

customer.append("j@j.com")

print(f" Lista con el dato nuevo al final: {customer}")

#Para agregar un elemento en una posición especifica

customer.insert(2, "holas")

print(f"Lista con un elemento en el puesto #2: {customer}")

#Ver tamaño lista

print(len(customer))

contar = 0;

while contar < len(customer):
    print(customer[contar])
    contar +=1

index = 0

lista_en_blanco = []

#while index < 5:
    #user_input = input(f"Ingrese un texto # {index + 1}: ")
    #lista_en_blanco.append(user_input)
    #index += 1;

print(f"Lista resultante: {lista_en_blanco}")

"""
 !#For loop
"""
 
print("\n\n------------------------------------------------- \nFor loop\n")


ages = [2,4,1,5,3,2,7,4]

#for in

for i in range(len(ages)):
    print(f"Edades en for-in: {ages[i]}")

# List Comprehension

ages2 = [i for i in ages if i > 3]

print("Ages2:")
print(ages2)

print("\n\n------------------------------------------------- \nList Methods\n")

# headers = ["Identificacion", "Nombre", "Apellido", "Salario", "Telefono", "Activo", "Correo"]

# customer = []

#for i in range(len(headers)):
    
    #if(headers[i] != "Activo"):
        #user_input = input(f"Ingrese su {headers[i]}: ")
        #customer.append(user_input)
    #else:
        #user_input = input(f"Ingrese su estado (Activo o Inactivo): ")
        #customer.append(user_input)

    #for j in range(len(customer)):
        #if i == j:
            #print(f"{headers[i]} : {customer[j]}")
            #continue



print("\n\n------------------------------------------------- \nTuplas\n")
# """
# !# Tuplas
#  - Inmutables
#  - Usado para definir colecciones de elementos fijos
#  - Se crean con ()
#  - Se pueden actualizar pero no se puede agregar elementos (Se podría pero casteandolo a list)
#
#  ?# Metodos: 
#  .count(x) cuenta la cantidad de veces que aparece x elemento
# """

# headers_tupla = tuple(headers)

# print(type(headers_tupla))


print("\n\n------------------------------------------------- \nDiccionarios\n")

"""
!# Diccionarios
- No permite duplicados en las llaves
- Son ordenados

?# Metodos especiales:
    - .get() -> para obtener el valor de la llave
    - .update()	Updates the dictionary with the specified key-value pairs

"""
customer_dict = {
    "id": 801081,
    "name": "Pepito"
}

# customer2_dict = {701: ["PP", "perez"], 702: ["Lu", "Sia"]}
#
# print(customer_dict.get("id"))
#
# #Primera forma para agregar elementos a los dics
# customer2_dict[703] = ["ola", "no"]
#
# print(customer2_dict)
#
# #Segunda forma para agregar elementos a los dics
#
# customer2_dict.update({704:["hola"]})
#
# print(customer2_dict)

#Agregar elementos a la lista

print("\n\n------------------------------------------------- \nSets\n")

"""
!Sets

- No son ordenados
- No son indexados
- No permiten cambiar los elementos existenten
- No permiten duplicados
"""
color = {"Amarillo", "Azul", "Rojo"}

#print(color) #{'Amarillo', 'Rojo', 'Azul'}


print("\n\n------------------------------------------------- \nMatch\n")

option = int(input("Seleccione: \n1. Registro \n2. Login \n3. Cerrar\n\n"))

match option:
    case 1:
        print("Registro")
    case 2:
        print("Login")
    case 3:
        print("Cerrar")
    case _:
        print("Opción no valida")


