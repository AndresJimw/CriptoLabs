from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import base64
import hashlib

def generate_key(password):
    key = hashlib.sha256(password.encode('utf-8')).digest()
    return key

def encrypt(plaintext, key):
    cipher = ChaCha20.new(key=key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt(ciphertext, key):
    cipher = ChaCha20.new(key=key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    password = 'qwerty'  # Contraseña
    key = generate_key(password)

    plaintexts = [
        b'e47a2bfe646a',
        b'ea783afc66',
        b'e96924f16d6e'
    ]

    for plaintext in plaintexts:
        plaintext_bytes = bytes.fromhex(plaintext.decode('utf-8'))
        ciphertext = encrypt(plaintext_bytes, key)
        print("Texto Plano: ", plaintext_bytes)
        print("Texto Cifrado (en Base64):", base64.b64encode(ciphertext).decode('utf-8'))
        decrypted_text = decrypt(ciphertext, key)
        print("Texto Descifrado: ", decrypted_text)
        print()

if __name__ == "__main__":
    main()
