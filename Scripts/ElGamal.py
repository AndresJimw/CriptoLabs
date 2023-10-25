import random

# Paso 1: Generar un número primo grande p
p = 17  # Número primo

# Paso 2: Encontrar un elemento primitivo α ∈ Z∗p
alpha = 6  # Elemento primitivo

# Paso 3: Elegir una clave privada aleatoria d ∈ {2, 3....p − 2}
d = 5

# Paso 4: Calcular la clave pública β = α^d (mod p)
beta = (alpha ** d) % p

# Mostrar clave pública y privada
print("Clave pública (Kpub):", (p, alpha, beta))
print("Clave privada (Kpr):", (p, d))

# Paso 5: Encriptar un mensaje x ∈ Z∗p
x = random.randint(2, p - 1)  # Mensaje aleatorio
i = random.randint(2, p - 2)  # Número aleatorio i
kEphemeral = (alpha ** i) % p  # Calcular clave efímera
kMasking = (beta ** i) % p  # Calcular clave de enmascaramiento
y = (x * kMasking) % p  # Encriptar el mensaje

# Mostrar mensaje encriptado y claves efímera y de enmascaramiento
print("Mensaje encriptado (kE, y):", (kEphemeral, y))
print("Clave de enmascaramiento (kM):", kMasking)

# Paso 6: Desencriptar el mensaje x: x ≡ y · k^(-1)M (mod p)
kMaskingInverse = pow(kMasking, -1, p)  # Calcular inverso multiplicativo de la clave de enmascaramiento
decrypted_message = (y * kMaskingInverse) % p  # Desencriptar el mensaje

# Mostrar mensaje desencriptado
print("Mensaje desencriptado (x):", decrypted_message)
