# Programa: Analizador de Calidad y Errores numéricos
# Objetio: Demostrar errores de redondeo y precisión en Python

import math
from decimal import Decimal

# 1. FUNCIÓN PARA CÁLCULO DE ERRORES (Conceptos 1.2 y 1.3)
def analizar_errores(v_real, v_aprox):
    """Calcula y muestra los tres tipos de errores básicos."""
    error_abs = abs(v_real - v_aprox)
    error_rel = error_abs / abs(v_real)
    error_perc = error_rel * 100

    print(f"    > Error Absoluto:       {error_abs:.20f}")
    print(f"    > Error Relativo:       {error_rel:.20f}")
    print(f"    > Error Porcentual:     {error_perc:.20f}%")

# 2. EXPERIMENTO DE SUMA ACUMULADA (Error de Redondeo 1.3)
def experimento_sumas(valor_a_sumar, repeticiones):
    """Suma un npumero muchas veces para ver cómo crece el error."""
    print(f"\n---  EXPERIMENTO: Sumando {valor_a_sumar} un total de {repeticiones} veces  ---")

    suma_computadora = 0.0
    for i in range(repeticiones):
        suma_computadora += valor_a_sumar

    valor_teorico = valor_a_sumar * repeticiones

    print(f"Resultado Teórico:      {valor_teorico}")
    print(f"Resultado Computadora:  {suma_computadora}")

    # Llamamos a nuestra función de errores para comparar
    analizar_errores(valor_teorico, suma_computadora)

# --- BLOQUE PRINCIPAL (EJECUCIÓN) ---
print("BIENVENIDOS AL LABORATORIO NUMÉRICO")
print("="*35)

# CASO A: El problema del 0.1 (Error de Redondeo Binario)
experimento_sumas(0.1, 100)  # Debería dar 10.0 exacto

# CASO B: El problema de la Precisión Extrema (Cifras Significativas)
print("\n--- COMPARACIÓN DE PRECISIÓN (PI) ---")
pi_computadora = 3.141592653589793  # Float estándar
pi_decimal = Decimal('3.1415926535897932384626433832') # Precisión alta

print(f"PI (math.pi):         {math.pi}")
print(f"PI (Manual float):    {pi_computadora}")
print(f"PI (Decimal):         {pi_decimal}")

# Verificamos error entre math.pi y una versión truncada
print("\nAnálisis de aproximación PI = 3.1416:")
analizar_errores(3.14159, 3.14)
