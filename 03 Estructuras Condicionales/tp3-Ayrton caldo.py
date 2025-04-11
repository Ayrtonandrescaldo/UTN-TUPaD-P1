#ejercicio 1 
 
edad = int(input("ingrese su edad: ")) 
if edad >= 18: 
    print("es mayor de edad") 
 
#ejercicio 2 
 
nota = int(input("ingrese una nota: ")) 
if nota >= 6 : 
    print("aprobado") 
else: 
    print("desaprobado") 
 
#ejercicio 3 
 
num = int(input("ingrese un numero: ")) 
if num % 2 == 0: 
    print("el numero es par") 
else: 
    print("el numero es impar") 
 
 #ejercicio 4 
 
 edad_como_cadena = input("ingrese su edad: ") 
edad = int(edad_como_cadena) 
if edad >= 0 and edad < 12: 
    print("es un niño") 
elif edad >= 12 and edad < 18: 
    print("es un adolescente") 
elif edad >= 12 and edad <= 17: 
    print("Adolescente") 
elif edad >= 18 and edad < 30: 
    print("adulto/a joven") 
elif edad >= 30: 
    print("adulto/a") 
else: 
    print("Edad inválida") 
 
#ejercicio 5  
#    
contraseña = str(input("Ingrese la contraseña:"))  
if len(contraseña) >= 8 and len(contraseña) <= 14: 
    print("ha ingresado una contraseña correcta") 
else: 
    print("por favor, ingrese una contraseña de entre 8 y 14 caracteres") 
 
#ejercicio 6  
 
input("ingrese una letra para iniciar: ") 
from statistics import mode, median, mean 
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]  
print(numeros_aleatorios) 
moda = float(mode(numeros_aleatorios)) 
mediana = float(median(numeros_aleatorios)) 
media = float(mean(numeros_aleatorios)) 
if media > mediana and mediana > moda:  
    print("Hay un sesgo positivo") 
elif media < mediana and mediana < moda:  
    print("Hay un sesgo negativo") 
elif media == mediana and mediana == moda:  
    print("No hay un sesgo") 
 
#ejercicio 7 
 
frase = str(input("Ingrese una frase: "))  
frase_minusculas = str(frase.lower()) 
vocales = ["a","e","i","o","u"] 
if frase_minusculas[-1] in vocales:  
    print(f"{frase}!")  
else: 
    print(frase) 
 
#ejercicio 8 
 
nombre = str(input("ingrese su nombre: ")) 
print(     " ¿que desea realizar con el nombre ingresado?  "    ) 
print( " (1) su nombre completo en mayuscula    "  ) 
print( " (2) su nombre en minusculas  "    )    
print( " (3) su nombre con la primer letra en mayuscula  "   ) 
numero = int(input("ingrese el numero de la opcion a realizar: ")) 
if numero == 1: 
    print(nombre .upper()) 
if numero == 2: 
    print(nombre .lower()) 
if numero == 3: 
    print(nombre .title())  
else: 
    print("fin")

#ejercicio 9

magnitud = float(input(" ingrese la magnitud: "))
if magnitud < 3:
print(" muy leve (inperceptible)")
elif magnitud >= 3 and magnitud < 4 :
print(" leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
print(" moderado (sentido por personas, pero generalmente no causa
daños)")
elif magnitud >= 5 and escala < 6:
print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
print("muy fuerte ( puede causar daños significativos)")
elif magnitud >= 7 :
print(" EXTREMO (puede causar daños a gran escala)")
else:
print()
#ejercicio 10
hemisferio = str(input("Ingrese en que hemisferio en el que se encuentra
(norte (N) o sur (S)): "))
mes = str(input("Ingrese su mes actual: "))
dia = int(input("Ingrese que numero de dia es hoy: " ))
if hemisferio == "N":
match mes:
case "enero" | "febrero":
print("se encuentra en Invierno")
case "marzo":
if dia <= 20:
print("Se encuentra en Invierno")
elif dia >= 21:
print("se encuentra en Primavera")
case "abril" | "mayo":
print("se encuentra en Primavera")
case "junio":
if dia <= 20:
print("se encuentra en Primavera")
elif dia >= 21:
print("se encuentra en Verano")
case "julio" | "agosto":
print("se encuentra en Verano")
case "septiembre":
if dia <= 20:
print("se encuentra en Verano")
elif dia >= 21:
print("se encuentra en Otoño")
case "octubre" | "noviembre":
print("se encuentra en Otoño")
case "diciembre":
if dia <= 20:
print("se encuentra en Otoño")
elif dia >= 21:
print("se encuentra en Invierno")
elif hemisferio == "S":
match mes:
case "enero" | "febrero":
print("se encuentra en Verano")
case "marzo":
if dia <= 20:
print("se encuentra en Verano")
elif dia >= 21:
print("se encuentra en Otoño")
case "abril" | "mayo":
print("se encuentra en Otoño")
case "junio":
if dia <= 20:
print("se encuentra en Otoño")
elif dia >= 21:
print("se encuentra en Invierno")
case "julio" | "agosto":
print("Se encuentra en Invierno")
case "septiembre":
if dia <= 20:
print("se encuentra en Invierno")
elif dia >= 21:
print("se encuentra en Primavera")
case "octubre" | "noviembre":
print("se encuentra en Primavera")
case "diciembre":
if dia <= 20:
print("se encuentra en Primavera")
elif dia >= 21:
print("se encuentra en Verano")    