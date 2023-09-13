from Crypto.Cipher import DES
import binascii
from Crypto.Util.Padding import unpad

# Introduce el texto cifrado en formato hexadecimal como cadena
cipher_text = input('Introduce el texto cifrado en formato hexadecimal: ')
key_text = input('Introduce la clave de cifrado (8 bytes): ')

def decrypt_des_ecb(cipher_text, key_text):
    # Convierte el texto cifrado en bytes desde la representación hexadecimal
    cipher_bytes = binascii.unhexlify(cipher_text)

    # Convierte la clave en bytes si aún está en formato de cadena
    key = key_text.encode('utf-8') if isinstance(key_text, str) else key_text

    # Crea un objeto DES en modo ECB
    cipher = DES.new(key, DES.MODE_ECB)

    # Desencripta el texto cifrado y utiliza unpad para eliminar el relleno
    plaintext_bytes = unpad(cipher.decrypt(cipher_bytes), DES.block_size)

    return plaintext_bytes.decode('utf-8')

try:
    decrypted_text = decrypt_des_ecb(cipher_text, key_text)
    print("Texto Plano Desencriptado: ", decrypted_text)
except Exception as e:
    print("Error al desencriptar: ", str(e))
