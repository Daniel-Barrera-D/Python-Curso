#Ejercicio 2
n1 = int(input("Ingrese numero 1: "))
n2 = int(input("Ingrese numero 2: "))
n3 = int(input("Ingrese numero 3: "))

if n1>=n2 and n1>=n3:
    print(f"{n1} es el numero mayor")
elif n2>=n1 and n2>=n3:
    print(f"{n2} es el numero mayor")
else:
    print(f"{n3} es el numero mayor")