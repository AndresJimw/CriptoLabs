from Crypto.Cipher import AES
import hashlib
import binascii
from Crypto.Util.Padding import unpad

cipher_text = input('Introduce el texto cifrado en formato hexadecimal: ')
password = input('Introduce la contraseña: ')

def decrypt_aes_ecb(cipher_text, password):
    # Convierte la contraseña en una clave de 32 bytes (256 bits) utilizando SHA-256
    key = hashlib.sha256(password.encode('utf-8')).digest()

    # Convierte el texto cifrado en bytes desde la representación hexadecimal
    cipher_bytes = binascii.unhexlify(cipher_text)

    # Crea un objeto AES en modo ECB
    cipher = AES.new(key, AES.MODE_ECB)

    # Desencripta el texto cifrado
    plaintext_bytes = cipher.decrypt(cipher_bytes)

    # Elimina el relleno CMS utilizando unpad de la biblioteca Crypto.Util.Padding
    plaintext = unpad(plaintext_bytes, AES.block_size)

    return plaintext.decode('utf-8')

try:
    decrypted_text = decrypt_aes_ecb(cipher_text, password)
    print("Texto Plano Desencriptado: ", decrypted_text)
except Exception as e:
    print("Error al desencriptar: ", str(e))
