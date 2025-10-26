from gestion_inventario import inventario

def analizar_componente(componente_dict):
    lecturas = componente_dict.get("lecturas", [])
    if not lecturas:
        return {"promedio": None, "max": None, "min": None}

    promedio = sum(lecturas) / len(lecturas)
    maximo = max(lecturas)
    minimo = min(lecturas)

    return {"promedio": promedio, "max": maximo, "min": minimo}
