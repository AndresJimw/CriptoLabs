from Crypto.Cipher import DES
import hashlib
import binascii
import sys

def encrypt_des(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_des(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def pad_pkcs7(data, block_size=8):
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length]) * padding_length
    return data + padding

def unpad_pkcs7(data):
    padding_length = data[-1]
    return data[:-padding_length]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python D1.py <mensaje> <clave>")
        sys.exit(1)

    plaintext = sys.argv[1]
    password = sys.argv[2]

    key = hashlib.md5(password.encode()).digest()[:8]

    print("Message:", plaintext)
    print("Key:", binascii.hexlify(key).decode())

    plaintext = plaintext.encode()
    padded_data = pad_pkcs7(plaintext)
    print("Padded (PKCS7):", binascii.hexlify(bytearray(padded_data)).decode())

    ciphertext = encrypt_des(padded_data, key)
    print("Cipher (DES ECB):", binascii.hexlify(bytearray(ciphertext)).decode())

    decrypted_data = decrypt_des(ciphertext, key)
    unpadded_data = unpad_pkcs7(decrypted_data)
    print("Decrypted and Unpadded:", unpadded_data.decode())
