#Ejercicio 1
reporte = "ID_SENSOR:T-21,LOC:Planta_Norte,TEMP:45.8,STATUS:OK"


partes = reporte.split(',')


id_sensor = partes[0].split(':')[1]
ubicacion = partes[1].split(':')[1]
temperatura = float(partes[2].split(':')[1])
estado = partes[3].split(':')[1]


print("*** REPORTE DE SENSOR ***")
print(f"ID: {id_sensor}")
print(f"Ubicación: {ubicacion}")
print(f"Temperatura: {temperatura} °C")
print(f"Estado: {estado}")
#1