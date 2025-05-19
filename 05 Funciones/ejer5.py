def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese los segundos a convertir: "))
print(f"La cantidad de horas es: {segundos_a_horas(segundos)}")