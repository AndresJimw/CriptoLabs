# Orden de un Elemento y Elemento Primitivo:
# Orden de un Elemento: En un grupo, el orden de un elemento a, denotado como |a|, es el menor número positivo n tal que a^n = e,
# donde e es el elemento identidad del grupo. En otras palabras, el orden de a es el número más pequeño de veces que necesitas
# combinar a consigo mismo para obtener el elemento identidad.
# Elemento Primitivo (Generador): En un grupo cíclico, un elemento g se llama elemento primitivo o generador si su orden es igual
# al orden del grupo. En otras palabras, |g| = |G|, donde |g| es el orden del elemento g y |G| es el tamaño del grupo.

def calculate_order(element, n):
    # Función para calcular el orden de un elemento en un grupo cíclico de residuos módulo n.
    result = element
    order = 1
    
    # Bucle para calcular a^n hasta encontrar el elemento identidad (a^n mod n = 1)
    while result != 1:
        result = (result * element) % n
        order += 1
    
    return order

# Ejemplo del Grupo Cíclico:
# En el ejemplo, el grupo cíclico es el conjunto de los residuos módulo 7: {0, 1, 2, 3, 4, 5, 6}.
# El elemento para el que calculamos el orden es 3.

# Parámetros del Grupo Cíclico
n = 7

# Elemento para el cual queremos calcular el orden
element = 3

# Calcular el orden del elemento en el grupo cíclico de residuos módulo n
order = calculate_order(element, n)

# Mostrar resultados
# Resultado:
# El script calculará y mostrará el orden del elemento 3 en el grupo cíclico de residuos módulo 7.
print(f"El orden del elemento {element} en el grupo cíclico de residuos módulo {n} es: {order}")
