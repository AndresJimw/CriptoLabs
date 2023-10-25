import random

# Claves públicas y privadas dadas
p = 17
alpha = 6
beta = 7

# Texto plano a cifrar
x = 13

# Paso 1: Encriptar el mensaje
i = random.randint(2, p - 2)  # Número aleatorio i
kEphemeral = (alpha ** i) % p  # Calcular clave efímera
kMasking = (beta ** i) % p  # Calcular clave de enmascaramiento
y = (x * kMasking) % p  # Encriptar el mensaje

# Mostrar mensaje encriptado y claves efímera y de enmascaramiento
print("Mensaje encriptado (kE, y):", (kEphemeral, y))
print("Clave de enmascaramiento (kM):", kMasking)

# Paso 2: Desencriptar el mensaje
kMaskingInverse = pow(kMasking, -1, p)  # Calcular inverso multiplicativo de la clave de enmascaramiento
decrypted_message = (y * kMaskingInverse) % p  # Desencriptar el mensaje

# Mostrar mensaje desencriptado
print("Mensaje desencriptado (x):", decrypted_message)




# Explicación:
"""
En este algoritmo, se toma un texto plano x = 13 y se cifra utilizando las claves públicas proporcionadas (p, α, β)
y un número aleatorio i para generar las claves efímera y de enmascaramiento. Luego, se desencripta el mensaje cifrado
utilizando la clave de enmascaramiento inversa. Ten en cuenta que las claves efímera y de enmascaramiento varían cada vez que
se ejecuta el código debido al valor aleatorio de i.
"""