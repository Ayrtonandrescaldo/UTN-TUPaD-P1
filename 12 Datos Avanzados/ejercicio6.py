#ejercicio6
alumnos = {}
for i in range(3):
    nombre_alumno = input("nombre del alumno: ")
    notas = tuple(float(input(f"nota {j+1}: ")) for j in range(3))
    alumnos[nombre_alumno] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(nombre, "promedio:", promedio)