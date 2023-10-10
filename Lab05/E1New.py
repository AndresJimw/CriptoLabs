import hashlib
import sys
import binascii
import Padding
import random
from Crypto.Cipher import AES
from Crypto import Random

msg = "test"

def encrypt(word, key, mode):
    plaintext = pad(word)
    encobj = AES.new(key, mode)
    return encobj.encrypt(plaintext)

def decrypt(ciphertext, key, mode):
    encobj = AES.new(key, mode)
    rtn = encobj.decrypt(ciphertext)
    return rtn.rstrip(b"\0")  # Eliminar los caracteres de relleno

def pad(s):
    extra = len(s) % 16
    if extra > 0:
        s = s + (b' ' * (16 - extra))
    return s

rnd = random.randint(1, 2 ** 256)  # Generar un número aleatorio de 256 bits
keyA = hashlib.sha256(str(rnd).encode()).digest()
rnd = random.randint(1, 2 ** 256)  # Generar otro número aleatorio de 256 bits
keyB = hashlib.sha256(str(rnd).encode()).digest()

print('Long-term Key Alice=', binascii.hexlify(keyA))
print('Long-term Key Bob=', binascii.hexlify(keyB))

rnd = random.randint(1, 2 ** 256)  # Generar un tercer número aleatorio de 256 bits
keySession = hashlib.sha256(str(rnd).encode()).digest()

ya = encrypt(keySession, keyA, AES.MODE_ECB)
yb = encrypt(keySession, keyB, AES.MODE_ECB)

print("Encrypted key sent to Alice:", binascii.hexlify(ya))
print("Encrypted key sent to Bob:", binascii.hexlify(yb))

decipherA = decrypt(ya, keyA, AES.MODE_ECB)
decipherB = decrypt(yb, keyB, AES.MODE_ECB)

print("Session key:", binascii.hexlify(keySession).decode())
print("Decrypted session key by Alice:", binascii.hexlify(decipherA).decode())
print("Decrypted session key by Bob:", binascii.hexlify(decipherB).decode())
