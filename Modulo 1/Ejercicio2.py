while True:
    try:
        temp_caldera = float(input("Ingrese la temperatura de la caldera (°C): "))
        break
    except ValueError:
        print("Error: Ingrese un número válido para la temperatura.")

while True:
    try:
        presion_caldera = float(input("Ingrese la presión de la caldera: "))
        break
    except ValueError:
        print("Error: Ingrese un número válido para la presión.")

operador_input = input("¿Está el operador presente? (S/N): ").upper()
operador_presente = (operador_input == 'S')

condicion_riesgo_alto = (temp_caldera > 100.0) and \
                        (presion_caldera > 103.0)

condicion_descuido_critico = (temp_caldera > 105.0) and \
                             (operador_presente == False)

alarma_critica = condicion_riesgo_alto or condicion_descuido_critico

print("\n" + "=" * 40)
print("--- INFORME DE SEGURIDAD DE CALDERA ---")
print("=" * 40)
print(f"VALORES INGRESADOS:")
print(f"  Temperatura: {temp_caldera}°C")
print(f"  Presión: {presion_caldera}")
print(f"  Operador Presente: {operador_presente}")
print("-" * 40)

if alarma_critica:
    print("!!! ALARMA CRÍTICA: ¡ACTIVADA!")
    print("Se requiere acción inmediata para estabilizar el sistema.")
else:
    print("ALARMA CRÍTICA: Desactivada.")
    print("Condiciones dentro de los límites de monitoreo (por ahora).")

print("=" * 40)