from Crypto.Cipher import AES
import hashlib
import binascii
from Crypto.Util.Padding import unpad

val = '68656c6c6f'
password = 'hello123'

cipher = input('Ingresa el cifrado en formato hexadecimal: ')
password = input('Ingresa la contraseña: ')

plaintext = binascii.unhexlify(val)

def encrypt(plaintext, key, mode):
    encobj = AES.new(key, mode)
    return encobj.encrypt(plaintext)

def decrypt(ciphertext, key, mode):
    encobj = AES.new(key, mode)
    return encobj.decrypt(ciphertext)

key = hashlib.sha256(password.encode('utf-8')).digest()
ciphertext = binascii.unhexlify(cipher)

print("Texto cifrado (ECB): " + binascii.hexlify(bytearray(ciphertext)).decode('utf-8'))
plaintext = decrypt(ciphertext, key, AES.MODE_ECB)
plaintext = unpad(plaintext, AES.block_size).decode('utf-8')
print("Texto descifrado: " + plaintext)
