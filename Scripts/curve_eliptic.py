# Calculando los Puntos en la Curva Elíptica E sobre Z7
points_on_curve = []
for x in range(7):
    y_squared = (x ** 3 + 3 * x + 2) % 7
    # Verificar si existe un y^2 ≡ x^3 + 3x + 2 mod 7
    for y in range(7):
        if (y ** 2) % 7 == y_squared:
            points_on_curve.append((x, y))

# Orden del Grupo (Número de Puntos más el Elemento Neutro)
order_of_group = len(points_on_curve) + 1  # Se añade el elemento neutro (incluso si no está en la lista)

# Verificar si alfa es primitivo (si tiene el mismo orden que el grupo)
alpha = (0, 3)
is_alpha_primitive = alpha in points_on_curve and len(points_on_curve) == order_of_group - 1

# Mostrar Resultados
print("Puntos en la Curva Elíptica E sobre Z7:", points_on_curve)
print("Orden del Grupo:", order_of_group)
print("¿Alpha es Primitivo?:", is_alpha_primitive)


# Encabezado del Problema:
"""
Problema de la Curva Elíptica:
Dada la curva elíptica E definida sobre Z7: E: y^2 = x^3 + 3x + 2
1) Dado el elemento alfa = (0, 3), calcular todos los puntos en E sobre Z7.
2) ¿Cuál es el orden del grupo? (No olvidar el elemento neutro)
3) ¿Es alfa primitivo?
"""

# Explicaciones Detalladas:
"""
Explicaciones:
1) Para encontrar todos los puntos en la curva elíptica E sobre Z7, podemos verificar para cada x en Z7
   si existe un y tal que y^2 ≡ x^3 + 3x + 2 mod 7.
2) El orden del grupo es el número total de puntos en la curva más el elemento neutro del grupo.
   Para una curva elíptica sobre un cuerpo finito, el orden se puede calcular contando los puntos.
3) Alfa es primitivo si su orden es igual al orden del grupo.

Cómo Resolvemos el Problema:
1) Iteramos sobre x en Z7 y verificamos si existe un y tal que y^2 ≡ x^3 + 3x + 2 mod 7.
2) Contamos los puntos y añadimos el elemento neutro para encontrar el orden del grupo.
3) Verificamos si alfa tiene el mismo orden que el grupo.
"""