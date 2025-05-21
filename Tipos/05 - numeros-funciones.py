import math  # Módulo incluido de forma nativa en Python que contiene funciones matemáticas avanzadas

# Función round(): redondea el número al entero más cercano
print(round(1.3))  # Redondea 1.3 → 1 (más cerca de 1 que de 2)
print(round(1.5))  # Redondea 1.5 → 2 (cuando es .5, redondea hacia el par más cercano o hacia arriba en casos simples)
print(round(1.8))  # Redondea 1.8 → 2 (más cerca de 2)

# Función abs(): devuelve el valor absoluto de un número
print(abs(-77))    # Devuelve 77 (valor absoluto, siempre positivo)

# Python no tiene muchas funciones matemáticas avanzadas nativas.
# Para eso existe el módulo 'math', que ofrece herramientas adicionales como redondeos especiales, raíces, potencias, etc.

# Funciones del módulo math
print(math.ceil(1.1))  # ceil() redondea siempre hacia arriba → 2
print(math.floor(1.999999999999999999999999))  # floor() redondea siempre hacia abajo → 1
print(math.isnan(23))  # isnan() verifica si un valor "No Es Un Número" (NaN). 23 sí es número → False
print(math.pow(10, 3))  # pow() calcula potencias: 10 elevado a la 3 → 1000.0
print(math.sqrt(9))  # sqrt() calcula la raíz cuadrada: raíz de 9 → 3.0

# Nota: dentro de Google, buscando "python math module" se puede encontrar mucha más información
# sobre todas las funciones que ofrece el módulo math.
