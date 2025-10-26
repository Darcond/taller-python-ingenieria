#Ejercicio 2
def validar_codigo_lote(codigo_lote):
    """
    Valida un código de lote según las siguientes reglas:
    - Debe tener exactamente 12 caracteres.
    - Debe empezar con 'LOT-'.
    - Debe terminar con '-24'.
    - El 8vo carácter (índice 7) debe ser 'X' o 'Y'.
    """
    if (
        len(codigo_lote) == 12 and
        codigo_lote.startswith("LOT-") and
        codigo_lote.endswith("-24") and
        codigo_lote[7] in ["X", "Y"]
    ):
        return True
    else:
        return False



codigos_prueba = ["LOT-45A-X-B-24", "LOT-44B-Z-C-23"]

for codigo in codigos_prueba:
    if validar_codigo_lote(codigo):
        print(f"{codigo} Válido")
    else:
        print(f"{codigo} Inválido")

#2