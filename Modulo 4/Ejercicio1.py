from gestion_inventario import inventario

sensores = []
motores = []
valvulas = []

for componente in inventario:
    if componente["tipo"] == "Sensor":
        sensores.append(componente["id"])
    elif componente["tipo"] == "Motor":
        motores.append(componente["id"])
    elif componente["tipo"] == "Válvula":
        valvulas.append(componente["id"])

print("Clasificación de Componentes:")
print(f"  Sensores: {sensores}")
print(f"  Motores: {motores}")
print(f"  Válvulas: {valvulas}")
