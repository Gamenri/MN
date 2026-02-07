# --- Función 1: Calcula la diferencia simple entre valores ---
def obtener_error_absoluto(real, aprox):
    """Calcula el error absoluto: |Valor real - Valor Aproximado|"""
    resultado = abs(real - aprox)
    return resultado

# --- Función 2: Calcula qué tan grande es el error respecto al real ---
def obtener_error_relativo(error_abs, real):
    """Calcula el error relativo: Error absoluto / |Valor Real|"""
    if real != 0:
        # Aquí hay una incidencia de SEGUNDO NIVEL (dentro del if)
        relativo = error_abs / abs(real)
        return relativo
    else:
        return None

# --- Bloque Principal (la ejecución) ---
valor_verdadero = 3.14159265
lista_aproimaciones = [3.14, 3.1, 3.0]

print (f"Valor Real: {valor_verdadero}\n")

# Aqui usamos un ciclo 'for' para ver multiples niveles de indentación
for aprox in lista_aproimaciones:
    # NIVEL 1: Dentro del cuclo for
    err_abs = obtener_error_absoluto(valor_verdadero, aprox)
    err_rel = obtener_error_relativo(err_abs, valor_verdadero)

    print(f"Analizando aproximación: {aprox}")

    if err_rel < 0.01:
        # NIVEL 2: Dentro del if que está dentro del for
        print(" -> ¡Es una aproximación muy buena! (Menor al 1%)")

    else:
        # NIVEL 2: El 'else' también lleva su propio bloque indentado
        print(f" -> Error significativo: {err_rel:.4%}")

    print("-" * 30) # Final de una iteración
