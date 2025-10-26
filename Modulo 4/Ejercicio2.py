CAPACIDAD_MAXIMA = 1000.0
volumen_actual = 0.0
tasa_flujo = 50.5
minuto = 0

LIMITE_ALERTA = 950.0

print("--- INICIANDO SIMULACIÓN DE LLENADO DE TANQUE (1000L) ---")

while volumen_actual < CAPACIDAD_MAXIMA:
    minuto += 1

    volumen_actual += tasa_flujo
    if volumen_actual > LIMITE_ALERTA:
        if volumen_actual > CAPACIDAD_MAXIMA:
             volumen_actual = CAPACIDAD_MAXIMA
             
        print("-" * 45)
        print(f"[{minuto} min]: Volumen = {volumen_actual:.2f} L")
        print("!!! ALERTA: Tanque casi lleno. Deteniendo el flujo.")
        
        break
    
    print(f"[{minuto} min]: Volumen = {volumen_actual:.2f} L")

print("-" * 45)
print("Simulación de llenado detenida.")
print(f"Volumen final alcanzado: {volumen_actual:.2f} L")
print(f"Tiempo total: {minuto} minutos")