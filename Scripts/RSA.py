def gcd(a, b):
    # Calcula el máximo común divisor utilizando el algoritmo de Euclides
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi_n):
    # Calcula el inverso modular de 'e' en relación con 'phi_n' usando el algoritmo de Euclides extendido
    d = 0
    x1, x2, y1, y2 = 1, 0, 0, 1
    temp_phi_n = phi_n
    
    while e > 0:
        q = temp_phi_n // e
        temp_phi_n, e = e, temp_phi_n % e
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2
        
    if temp_phi_n == 1:
        d = y1 % phi_n
    
    return d

def generate_rsa_key_pair(p, q):
    # Paso 1: Calcular n = p * q
    n = p * q
    
    # Paso 2: Calcular φ(n) = (p - 1)(q - 1)
    phi_n = (p - 1) * (q - 1)
    
    # Paso 3: Elegir un pequeño número primo 'e' que sea coprimo con φ(n)
    e = 3  # En este caso, 3 es un número primo
    
    # Paso 4: Calcular el inverso modular de 'e' en relación con 'phi_n' para obtener 'd'
    d = mod_inverse(e, phi_n)
    
    # Claves generadas: (e, n) es la clave pública, (d, n) es la clave privada
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

# Números primos dados
p = 3
q = 11

# Generar par de claves RSA
public_key, private_key = generate_rsa_key_pair(p, q)

# Mostrar las claves generadas
print("Clave pública (e, n):", public_key)
print("Clave privada (d, n):", private_key)
