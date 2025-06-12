#ejercicio7
entrada_parcial1 = input("ingrese los legajos de los estudiantes que aprobaron el parcial 1, separados por espacio: ")
entrada_parcial2 = input("ingrese los legajos de los estudiantes que aprobaron el parcial 2, separados por espacio: ")

estudiantes_parcial1 = set(map(int, entrada_parcial1.strip().split()))
estudiantes_parcial2 = set(map(int, entrada_parcial2.strip().split()))

estudiantes_aprobaron_ambos = estudiantes_parcial1.intersection(estudiantes_parcial2)
estudiantes_aprobaron_solo_uno = estudiantes_parcial1.symmetric_difference(estudiantes_parcial2)
estudiantes_aprobaron_alguno = estudiantes_parcial1.union(estudiantes_parcial2)

print("estudiantes que aprobaron ambos parciales:", estudiantes_aprobaron_ambos)
print("estudiantes que aprobaron solo uno de los parciales:", estudiantes_aprobaron_solo_uno)
print("estudiantes que aprobaron al menos un parcial:", estudiantes_aprobaron_alguno)