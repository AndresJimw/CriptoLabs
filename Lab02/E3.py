from Crypto.Cipher import DES
import hashlib
import binascii
from Crypto.Util.Padding import unpad
import base64

base64_cipher_text = input('Introduce el texto cifrado en formato Base64: ')
password = input('Introduce la contraseña: ')

def decrypt_des_ecb(base64_cipher_text, password):
    # Convierte la contraseña en una clave de 8 bytes
    key = hashlib.sha256(password.encode('utf-8')).digest()[:8]

    # Decodifica el texto cifrado desde Base64
    cipher_bytes = base64.b64decode(base64_cipher_text)

    # Crea un objeto DES en modo ECB
    cipher = DES.new(key, DES.MODE_ECB)

    # Desencripta el texto cifrado
    plaintext_bytes = cipher.decrypt(cipher_bytes)

    # Elimina el relleno CMS utilizando unpad de la biblioteca Crypto.Util.Padding
    plaintext = unpad(plaintext_bytes, DES.block_size)

    return plaintext.decode('utf-8')

try:
    decrypted_text = decrypt_des_ecb(base64_cipher_text, password)
    print("Texto Plano Desencriptado: ", decrypted_text)
except Exception as e:
    print("Error al desencriptar: ", str(e))
