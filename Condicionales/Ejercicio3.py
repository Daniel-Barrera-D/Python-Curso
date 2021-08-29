#Ejercicio 4
nombre1 = input("Nombre 1: ")
nombre2 = input("Nombre 2: ")
if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
    print("Si hay coincidencia")
else:
    print("No hay coincidencia")