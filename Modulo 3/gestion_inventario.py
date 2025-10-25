# Base de Datos de Componentes
inventario = [
    {
        "id": "S-101",
        "tipo": "Sensor",
        "ubicacion": "Zona A",
        "lecturas": [23.5, 24.0, 22.8]
    },
    {
        "id": "M-202",
        "tipo": "Motor",
        "ubicacion": "Zona B",
        "lecturas": [1500.0, 1520.5, 1495.3]
    },
    {
        "id": "V-303",
        "tipo": "Válvula",
        "ubicacion": "Zona C",
        "lecturas": [1.2, 1.3, 1.1]
    }
]

# Cálculo del promedio de lecturas para un componente específico
id_buscar = "S-101"
for componente in inventario:
    if componente["id"] == id_buscar:
        promedio = sum(componente["lecturas"]) / len(componente["lecturas"])
        print(f"Promedio de lecturas para {id_buscar}: {promedio}")
        break
# Si no se encuentra el componente
else:
    print(f"Componente con id {id_buscar} no encontrado.")