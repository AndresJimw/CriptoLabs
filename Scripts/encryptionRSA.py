def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = (plaintext ** e) % n
    return ciphertext

# Valores dados
plaintext = 8
public_key = (3, 33)

# Cifrar el texto plano usando la clave pública
ciphertext = rsa_encrypt(plaintext, public_key)

# Mostrar el texto cifrado
print("Texto cifrado (C):", ciphertext)
