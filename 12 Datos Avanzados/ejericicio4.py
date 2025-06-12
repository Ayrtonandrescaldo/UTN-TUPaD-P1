#ejericio4
contactos = {}
for i in range(5):
    nombre = input("nombre: ")
    numero = input("número: ")
    contactos[nombre] = numero
consulta = input("consultar nombre: ")
if consulta in contactos:
    print(contactos[consulta])
else:
    print("no existe")

#ejercicio5
frase = input("frase: ")
palabras = frase.lower().split()
unicas = set(palabras)
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
print("palabras únicas:", unicas)
print("frecuencia:", frecuencia)