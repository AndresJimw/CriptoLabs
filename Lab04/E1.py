import rsa

# Generar un par de claves RSA de 512 bits
(bob_pub, bob_priv) = rsa.newkeys(512)

# Imprimir las claves públicas y privadas
print("Clave pública (bob_pub):")
print(f"N: {bob_pub.n}")  # Valor de N
print(f"E: {bob_pub.e}")  # Valor de e
print("\nClave privada (bob_priv):")
print(f"N: {bob_priv.n}")  # Valor de N
print(f"D: {bob_priv.d}")  # Valor de d

# Mensaje que deseamos cifrar
msg = 'Here is my message'

# Ciframos el mensaje utilizando la clave pública
ciphertext = rsa.encrypt(msg.encode(), bob_pub)

# Desciframos el mensaje utilizando la clave privada
message = rsa.decrypt(ciphertext, bob_priv)

# Imprimimos el mensaje descifrado
print(message.decode('utf8'))
