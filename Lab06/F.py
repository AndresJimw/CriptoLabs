import OpenSSL
from cryptography import x509
from cryptography.hazmat.backends import default_backend

filenames = ["fred.pfx", "bill01.pfx", "bill02.pfx", ..., "bill18.pfx", "country01.pfx", "country02.pfx", ..., "country06.pfx"]
passwords = ["ankle", "battery", "password", "bill", "apple", "apples", "orange"]  # Lista de contraseñas a probar

for filename in filenames:
    print(f"\nCrackeando contraseña para el archivo: {filename}")
    for password in passwords:
        try:
            pfx = open(filename, 'rb').read()
            p12 = OpenSSL.crypto.load_pkcs12(pfx, password)
            print(f"Contraseña encontrada: {password}")

            privkey = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey())
            cert = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate())
            cert = x509.load_pem_x509_certificate(cert, default_backend())

            print(" Emisor: ", cert.issuer)
            print(" Sujeto: ", cert.subject)
            print(" Número de serie: ", cert.serial_number)
            print(" Algoritmo de hash: ", cert.signature_hash_algorithm.name)
            print(privkey)
            print(cert)

        except Exception as e:
            print(f"No funciona con contraseña '{password}': {e}")
