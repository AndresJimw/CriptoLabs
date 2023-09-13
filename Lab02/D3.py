from Crypto.Cipher import AES
import hashlib
import binascii

def encrypt_aes(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_aes(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def pad_pkcs7(data, block_size=16):
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length]) * padding_length
    return data + padding

def unpad_pkcs7(data):
    padding_length = data[-1]
    return data[:-padding_length]

if __name__ == "__main__":
    cipher = input('Enter cipher: ')
    password = input('Enter password: ')

    key = hashlib.md5(password.encode()).digest()[:16]

    print("Cipher:", cipher)
    print("Key:", binascii.hexlify(key).decode())

    plaintext = binascii.unhexlify(cipher)
    decrypted_data = decrypt_aes(plaintext, key)
    unpadded_data = unpad_pkcs7(decrypted_data)
    print("Decrypted and Unpadded:", unpadded_data.decode())
