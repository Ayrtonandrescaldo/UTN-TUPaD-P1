#EJERCICIO-1

for i in range(0,101):
    print(i)

#EJERCICIO-2

num = int(input("ingrese un numero entero: "))
if num < 10 and num >= 0:
    print("el numero tiene un solo digito")
elif num >= 10 and num < 100:
    print("el numero tiene dos digitos")   
elif num >= 100 and num < 1000:
    print("el numero tiene tres digitos")  
elif num >= 1000 and num < 10000:
    print("el numero tiene cuatros digitos")
elif num >= 10000 and num < 100000:
    print("el numero tiene cinco digitos")
elif num >= 100000 and num < 1000000:
    print("el numero tiene seis digitos") 

#EJERCICIO-3 

 num1 = int(input("ingrese el primer numero entero: "))
num2 = int(input("ingrese el segundo numero entero: "))
suma = num1 + num2 
print("el resultado es " +suma)

#EJERCICIO-4

def suma():
    total = 0
    while True:
        num = int(input("Ingrese el (0) para detener: "))
        if num == 0:
            break
        total += num
    print("El total de la suma es:", total)

suma()

#EJERCICIO-5

import random

def adivinar_numero_aleatorio():
    numero_secreto = random.randint(0, 9)
    intentos = 0
    while True:
        numero_usuario = int(input("Ingrese un número entre 0 y 9: "))
        intentos += 1
        if numero_usuario < 0 or numero_usuario > 9:
            print("Número fuera de rango")
        elif numero_usuario < numero_secreto:
            print("Intente de nuevo.")
        elif numero_usuario > numero_secreto:
            print("Intente de nuevo.")
        else:
            print(f"Acertaste El número secreto era {numero_secreto}.")
            print(f"los intentos necesarios para adivinar fueron : {intentos}")
            break

adivinar_numero_aleatorio()

#EJERCICIO-6

print("bienvenido/a coloca una letra para comenzar:  ")
start = input()
def imprimir_pares():
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)

imprimir_pares()

#EJERCICIO-7

def suma():
    numero = int(input("Ingrese un número entero positivo: "))
    suma = 0

    for i in range(numero + 1):
        suma += i

    print(f"La suma de los números comprendidos entre 0 y {numero} es: {suma}")

suma()

#EJERCICIO-8

def contar_num():
    cantidad_num = 100
    impar = 0
    par= 0
    N = 0
    P = 0
    for i in range(cantidad_num):
        numero = int(input(f"Ingrese el número: "))
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
        if numero < 0:
            N += 1
        elif numero > 0:
            P += 1

    print(f"Pares: {par}")
    print(f"Impares: {impar}")
    print(f"Negativos: {N}")
    print(f"Positivos: {P}")

contar_num()

#EJERCICIO-9

def media_valores():
    suma = 0
    cantidad_num = 100
    
    for i in range(cantidad_num):
        num_ingresado = int(input(f"ingrese el numero: {i+1}:"))
        suma += num_ingresado
    media = suma / cantidad_num 
    print(f"la media de los numeros ingresados es {media}")
media_valores()

#EJERCICIO-10

def invertir_num():
    num = int(input("Ingrese un para invertirlo: "))
    numero_str = str(num)
    numero_invertido = numero_str[::-1]
    print(f"El número {num} invertido es: {numero_invertido}")

invertir_num()