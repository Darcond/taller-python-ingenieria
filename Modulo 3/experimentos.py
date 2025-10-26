equipo_A = {("EXP-001", "2023-10-01"), ("EXP-002", "2023-10-02"), ("EXP-003", "2023-10-03")}
equipo_B = {("EXP-002", "2023-10-02"), ("EXP-004", "2023-10-04"), ("EXP-001", "2023-10-01")}

# Operaciones con conjuntos
exitos_comunes = equipo_A & equipo_B
exitos_unicos = equipo_A | equipo_B
solo_equipo_A = equipo_A - equipo_B

# Impresión de resultados
print(f"\nExperimentos exitosos comunes: {exitos_comunes}")
print(f"Total de experimentos exitosos únicos: {len(exitos_unicos)}")
print(f"Experimentos solo realizados por equipo A: {solo_equipo_A}")