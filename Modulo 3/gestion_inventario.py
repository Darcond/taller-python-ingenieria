"""Gestor sencillo de inventario del Módulo 3.

Se expone una API mínima y un comportamiento por defecto al ejecutar el
archivo directamente. Esto facilita abrir/mostrar el inventario desde
la línea de comandos o desde otros módulos.
"""

# Lista de diccionarios (cada elemento representa un componente)
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


def obtener_inventario():
    """Devuelve la lista de componentes.

    Útil para importar desde otros módulos sin ejecutar la lógica de
    visualización.
    """
    return inventario


def calcular_promedio_lecturas(componente):
    """Calcula el promedio de las lecturas de un componente.

    Devuelve None si no hay lecturas.
    """
    lecturas = componente.get("lecturas") or []
    if not lecturas:
        return None
    return sum(lecturas) / len(lecturas)


def mostrar_inventario():
    """Imprime una vista legible del inventario y los promedios de lecturas."""
    inv = obtener_inventario()
    if not inv:
        print("Inventario vacío.")
        return

    print("Inventario de componentes:")
    for comp in inv:
        promedio = calcular_promedio_lecturas(comp)
        promedio_text = f"{promedio:.2f}" if promedio is not None else "N/A"
        print(f"- ID: {comp.get('id')} | Tipo: {comp.get('tipo')} | Ubicación: {comp.get('ubicacion')} | Promedio lecturas: {promedio_text}")


if __name__ == "__main__":
    # Comportamiento por defecto al ejecutar el archivo: mostrar inventario
    mostrar_inventario()