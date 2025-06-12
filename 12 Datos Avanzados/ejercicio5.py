#ejercicio5
frase = input("frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1
print("palabras únicas:", palabras_unicas)
print("frecuencia:", frecuencia_palabras)

