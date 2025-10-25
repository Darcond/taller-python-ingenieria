C = float(input("Ingrese la temperatura en grados Celsius (°C): "))

C = float(C)

F = C * (9/5) + 32
K = C + 273.15

print("-" * 35)
print(f"Temperatura Inicial: {C:.2f}°C")
print("-" * 35)
print(f"Equivalente en Fahrenheit (F): {F:.2f}°F")
print(f"Equivalente en Kelvin (K): {K:.2f} K")
print("-" * 35)