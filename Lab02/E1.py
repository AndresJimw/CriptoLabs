from Crypto.Cipher import AES
import hashlib
import binascii

def decrypt_aes(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def unpad_pkcs7(data):
    padding_length = data[-1]
    return data[:-padding_length]

if __name__ == "__main__":
    cipher_text = input('Enter CMS Cipher (256-bit AES ECB): ')
    password = input('Enter the encryption password: ')

    # Derivamos una clave de 32 bytes (256 bits) desde la contraseña
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), b'salt', 100000, dklen=32)

    cipher_text = binascii.unhexlify(cipher_text) 
    decrypted_data = decrypt_aes(cipher_text, key)
    unpadded_data = unpad_pkcs7(decrypted_data)
    print("Decrypted Plain text:", unpadded_data.decode())
