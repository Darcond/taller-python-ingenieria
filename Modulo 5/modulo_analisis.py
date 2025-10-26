import sys
import os
try:
    directorio_modulo_3 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Módulo 3'))
    
    if directorio_modulo_3 not in sys.path:
        sys.path.append(directorio_modulo_3)

    from gestion_inventario import inventario
except (ImportError, FileNotFoundError):
    print("ADVERTENCIA: Falló la importación de gestion_inventario.py. Usando inventario de muestra.")
   
    inventario = [
        {"id": "S-101", "tipo": "Sensor", "ubicacion": "Planta_Norte", "lecturas": [35.5, 36.1, 35.8]},
        {"id": "M-202", "tipo": "Motor", "ubicacion": "Zona_Sur", "lecturas": [120.5, 121.0, 119.9]},
        {"id": "S-105", "tipo": "Sensor", "ubicacion": "Planta_Norte", "lecturas": [33.0, 32.5, 34.0]},
    ]
def analizar_componente(componente_dict):
    """Calcula el promedio, máximo y mínimo de las lecturas de un componente."""
    
    lecturas = componente_dict.get("lecturas", [])
    
    if not lecturas:
      
        return {"promedio": None, "max": None, "min": None}
    
    promedio = sum(lecturas) / len(lecturas)
    maximo = max(lecturas)
    minimo = min(lecturas)

    return {"promedio": promedio, "max": maximo, "min": minimo}

if __name__ == "__main__":
    print("--- 5.1: Análisis de Componente (def) ---")
    
   
    if inventario:
        componente_prueba = inventario[0]
        resultados = analizar_componente(componente_prueba)
        print(f"Análisis del componente {componente_prueba['id']}: {resultados}")
    else:
        print("No hay inventario para probar la función.")


    print("\n--- 5.2: Filtrado y Mapeo Avanzado (lambda) ---")
    
    sensores_criticos_filter = filter(
        lambda comp: comp["tipo"] == "Sensor" and comp["ubicacion"] == "Planta_Norte",
        inventario
    )
    sensores_criticos = list(sensores_criticos_filter)
    
    ids_sensores = list(map(
        lambda comp: comp["id"],
        sensores_criticos
    ))

    print(f"Sensores críticos encontrados: {len(sensores_criticos)}")
    print(f"IDs de Sensores Críticos: {ids_sensores}")