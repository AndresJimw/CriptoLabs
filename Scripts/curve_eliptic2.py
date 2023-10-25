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

##############################################

# Preguntas sobre la curva elíptica E sobre Z7
# 4) ¿Cuántos puntos hay en la curva elíptica E sobre Z7?
total_points = len(points_on_curve)
print("Total de puntos en la Curva Elíptica E sobre Z7:", total_points)

# 5) ¿Cuáles son los puntos específicos en la curva elíptica E sobre Z7?
print("Puntos específicos en la Curva Elíptica E sobre Z7:", points_on_curve)

# 6) ¿Cuál es el orden de otros elementos en la curva elíptica E sobre Z7?
other_elements = [(1, 3), (2, 1), (3, 2), (4, 2), (5, 4), (6, 4)]
for element in other_elements:
    order = 1  # Inicia con 1 para incluir el elemento neutro
    x, y = element
    while (x, y) != (0, 0):  # Mientras no sea el elemento neutro
        x_squared = (x ** 3 + 3 * x + 2) % 7
        y_squared = (y ** 2) % 7
        if x_squared == y_squared:
            order += 1
        x, y = (x + 1) % 7, (y + 1) % 7  # Siguiente punto en la curva
    print(f"Orden del elemento {element} en la Curva Elíptica E sobre Z7: {order}")

# 7) ¿Cómo se calcula el inverso multiplicativo de un número en Z7?
def multiplicative_inverse(n, p):
    for i in range(1, p):
        if (n * i) % p == 1:
            return i
    return None

number = 3
inverse = multiplicative_inverse(number, 7)
print(f"Inverso multiplicativo de {number} en Z7: {inverse}")

# 8) ¿Qué otros elementos en Z7 pueden ser elementos primitivos en la curva elíptica E?
primitive_elements = []
for element in range(1, 7):
    is_primitive = True
    for i in range(2, 7):
        if (element ** i) % 7 == 1:
            is_primitive = False
            break
    if is_primitive:
        primitive_elements.append(element)
print("Elementos primitivos en Z7 para la Curva Elíptica E:", primitive_elements)


"""
¿Cuántos puntos hay en la curva elíptica E sobre Z7?
¿Cuáles son los puntos específicos en la curva elíptica E sobre Z7?
¿Cuál es el orden de otros elementos en la curva elíptica E sobre Z7?
¿Cómo se calcula el inverso multiplicativo de un número en Z7?
¿Qué otros elementos en Z7 pueden ser elementos primitivos en la curva elíptica E?

"""