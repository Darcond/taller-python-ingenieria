from gestion_inventario import inventario
sensores_criticos = list(filter(
    lambda comp: comp["tipo"] == "Sensor" and comp["ubicacion"] == "Planta_Norte",
    inventario
))

# Mapeo
ids_sensores = list(map(
    lambda comp: comp["id"],
    sensores_criticos
))

print(f"Sensores críticos encontrados: {len(sensores_criticos)}")
print(f"IDs de Sensores Críticos: {ids_sensores}")
