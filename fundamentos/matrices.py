edades = [[21,12,5], [34,25,16]] #matriz 2x3

for edad in edades:
    print(f'edades normales: {edad}')

edades_mayores = [65, 78, 81]

edades.append(edades_mayores)


for edad in enumerate(edades):
    print(f'Edades + Edades mayores: {edad}')