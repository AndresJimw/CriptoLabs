import random

# Paso 1: Generar un número primo grande p
p = 17  # Número primo

# Paso 2: Encontrar un elemento primitivo α ∈ Z∗p
alpha = 77  # Elemento primitivo

# Paso 3: Elegir una clave privada aleatoria d ∈ {2, 3....p − 2}
d = 10

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


## Cálculos 
kMasking = (beta ** i) % p
print('Resultado', (77*9) % 17)
print('Resultado 2:', (12 % 17))


print('Resultado 3:', (7**11 % 17))

print('Resultado 4:', ((12-10*14)))
print('Resultado 5:', ((-128)/11))

print('Resultado 6:', ((2*16) % 16))
print('Resultado 6:', ((3*11) % 16))
print('Resultado 7:', ((-128*3)))
print('Resultado 8:', ((16*25)))
print('Resultado 8:', ((16**0)))

print('Resultado 9:', ((11**14) % 17))
print('Resultado 10:', ((7**12) % 17))






