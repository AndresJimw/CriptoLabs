# Datos del Problema
alpha = 2   # Elemento primitivo en el subgrupo con 23 elementos
beta = 36   # Valor dado
p = 47      # Número primo, tamaño del grupo

# Bucle para encontrar el exponente x
for x in range(1, 24):  # x debe estar en el rango de 1 a 23 inclusive
    # Calculamos 2^x modulo 47
    result = (alpha ** x) % p
    
    # Comparamos el resultado con el valor dado beta
    if result == beta:
        # Si son iguales, hemos encontrado el exponente x
        break

# Mostrar el resultado
print("El exponente x tal que 2^x ≡ 36 mod 47 es:", x)

# Encabezado del Problema:
"""
Problema del Logaritmo Discreto:
Dado el grupo Z∗47 con orden 46, donde α = 2 es un elemento primitivo en un subgrupo de 23 elementos,
y β = 36, encontrar el exponente positivo x, 1 <= x <= 23, tal que 2^x ≡ 36 mod 47.
"""

# Explicaciones Detalladas:
"""
Explicaciones:
- El grupo Z∗47 tiene orden 46, lo que significa que hay 46 elementos en el grupo.
- Se menciona que hay subgrupos en Z∗47 con cardinalidad de 23, 2 y 1.
- Se nos dice que α = 2 es un elemento en el subgrupo con 23 elementos y es un elemento primitivo en ese subgrupo.
- El problema nos pide encontrar un exponente x tal que 2^x ≡ 36 mod 47, donde 1 <= x <= 23.

Cómo Resolvemos el Problema:
- Como α = 2 es un elemento primitivo en el subgrupo con 23 elementos, podemos calcular 2^x para x en el rango de 1 a 23
  y verificar si coincide con β = 36 mod 47.
- Cuando encontramos un valor de x que satisface la congruencia, hemos encontrado la solución al problema.
"""
