def gcd(a, b):
    # Calcula el máximo común divisor utilizando el algoritmo de Euclides
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime(e, phi_n):
    # Verifica si 'e' y 'phi_n' son coprimos
    return gcd(e, phi_n) == 1

# Valores de 'e' y φ(n) dados
e = 3  # Puedes cambiar este valor para probar diferentes números primos 'e'
phi_n = 8  # φ(n) para el ejemplo dado

# Verificar si 'e' y φ(n) son coprimos
if is_coprime(e, phi_n):
    print(f"{e} y φ({phi_n}) son coprimos.")
else:
    print(f"{e} y φ({phi_n}) no son coprimos.")
