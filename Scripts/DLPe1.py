# Datos del Problema
alpha = 5  # Elemento primitivo
beta = 41  # Valor dado
p = 47     # Número primo, tamaño del grupo

# Inicializamos el exponente a 1
x = 1

# Bucle para encontrar el exponente x
while True:
    # Calculamos 5^x modulo 47
    result = (alpha ** x) % p
    
    # Comparamos el resultado con el valor dado beta
    if result == beta:
        # Si son iguales, hemos encontrado el exponente x
        break
    else:
        # Si no son iguales, incrementamos el exponente y continuamos el bucle
        x += 1

# Mostrar el resultado
print("El exponente x tal que 5^x ≡ 41 mod 47 es:", x)






# Encabezado del Problema:
"""
Problema del Logaritmo Discreto:
Dado un grupo Z∗p, donde α = 5 es un elemento primitivo, y β = 41,
encontrar el exponente positivo x tal que 5^x ≡ 41 mod 47.
"""

# Explicaciones Detalladas:
"""
Datos del Problema:
alpha: Elemento primitivo del grupo.
beta: Valor dado que queremos igualar.
p: Número primo que define el grupo Z∗p.

Bucle para Encontrar el Exponente x:
El bucle while se ejecuta hasta encontrar un exponente x tal que 5^x ≡ 41 mod 47.
Calculamos 5^x mod 47 en cada iteración del bucle y comparamos el resultado con 41.
Si encontramos un x que satisface la condición, salimos del bucle.

Mostrar el Resultado:
Finalmente, mostramos el exponente x que cumple con la congruencia 5^x ≡ 41 mod 47.
"""
