# Obtener datos del usuario
n1 = input("Ingresa el primer numerillo")  # Solicita al usuario que ingrese el primer número
n2 = input("Ingresa el segundo numerillo")  # Solicita al usuario que ingrese el segundo número

# Convertir los datos ingresados (que son tipo str) a enteros
n1 = int(n1) 
n2 = int(n2)

# Mostrar la suma de los dos números (antes de guardarla en una variable)
print(n1 + n2)  # Realiza la suma correctamente ahora que ambos valores son enteros

# Realizar las operaciones básicas
suma = n1 + n2       # Suma de los dos números
resta = n1 - n2      # Resta entre los dos números
multi = n1 * n2      # Multiplicación de los dos números
div = n1 / n2        # División entre los dos números

# Crear un mensaje con los resultados usando formato multilínea
mensaje = f"""
Para los números {n1} y {n2}:
- El resultado de la suma es: {suma}.
- El resultado de la resta es: {resta}.
- El resultado de la multiplicación es: {multi}.
- El resultado de la división es: {div}.
"""

# Mostrar el mensaje final
print(mensaje)
