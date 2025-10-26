inventario = [
    {
        "id": "S-101",
        "tipo": "Sensor",
        "ubicacion": "Torre Norte",
        "lecturas": [23.4, 25.1, 24.7]
    },
    {
        "id": "M-202",
        "tipo": "Motor",
        "ubicacion": "Planta 1",
        "lecturas": [1500.0, 1498.5, 1502.3]
    },
    {
        "id": "V-303",
        "tipo": "Válvula",
        "ubicacion": "Línea Principal",
        "lecturas": [2.5, 2.6, 2.4]
    }
]

id_objetivo = "S-101"

for componente in inventario:
    if componente["id"] == id_objetivo:
        promedio_lecturas = sum(componente["lecturas"]) / len(componente["lecturas"]) #operación promedio
        print(f"Promedio de lecturas para el componente {id_objetivo}: {promedio_lecturas:.2f}")
        break