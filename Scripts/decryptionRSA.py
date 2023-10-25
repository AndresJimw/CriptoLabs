def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = (ciphertext ** d) % n
    return plaintext

# Función para descifrar usando la clave privada
def rsa_decrypt_with_example():
    # Valores dados
    ciphertext = 17
    private_key = (7, 33)
    
    # Descifrar el texto cifrado usando la clave privada
    decrypted_text = rsa_decrypt(ciphertext, private_key)
    
    # Mostrar el texto plano descifrado
    print("Texto plano descifrado (p):", decrypted_text)

# Llamar a la función para descifrar con los valores proporcionados
rsa_decrypt_with_example()
