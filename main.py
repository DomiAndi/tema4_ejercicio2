#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
numero_inicial = int(input("Introduce un numero: "))
numero_final = int(input("Introduce otro numero: "))
numeros_impares = []

while numero_final <= numero_inicial:
    numero_final  = int(input("El segundo numero debe ser mayor que el primero. Inroduce otro numero: "))

    for i in range(numero_inicial, numero_final+1):
        if(i % 2 != 0):
            numeros_impares.append(i)

print(f"Lista de Numeros impares entre {numero_inicial} y {numero_final}:")
print(numeros_impares)