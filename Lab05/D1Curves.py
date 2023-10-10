from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import binascii

sizeSECP256K1 = 256

# SECP256K1 Curve
Bob_private_key_secp256k1 = ec.generate_private_key(ec.SECP256K1(), default_backend())
Alice_private_key_secp256k1 = ec.generate_private_key(ec.SECP256K1(), default_backend())

Bob_shared_key_secp256k1 = Bob_private_key_secp256k1.exchange(ec.ECDH(), Alice_private_key_secp256k1.public_key())
Bob_derived_key_secp256k1 = HKDF(algorithm=hashes.SHA256(), length=sizeSECP256K1, salt=None, info=b'', backend=default_backend()).derive(Bob_shared_key_secp256k1)

Alice_shared_key_secp256k1 = Alice_private_key_secp256k1.exchange(ec.ECDH(), Bob_private_key_secp256k1.public_key())
Alice_derived_key_secp256k1 = HKDF(algorithm=hashes.SHA256(), length=sizeSECP256K1, salt=None, info=b'', backend=default_backend()).derive(Alice_shared_key_secp256k1)

print("SECP256K1 Curve:")
print("Name of curve:", Bob_private_key_secp256k1.public_key().curve.name)
print(f"Generated key size: {sizeSECP256K1} bytes ({sizeSECP256K1*8} bits)")
print("Bob's derived key: ", binascii.b2a_hex(Bob_derived_key_secp256k1).decode())
print("Alice's derived key: ", binascii.b2a_hex(Alice_derived_key_secp256k1).decode())

# SECP192R1 Curve
sizeSECP192R1 = 192

Bob_private_key_secp192r1 = ec.generate_private_key(ec.SECP192R1(), default_backend())
Alice_private_key_secp192r1 = ec.generate_private_key(ec.SECP192R1(), default_backend())

Bob_shared_key_secp192r1 = Bob_private_key_secp192r1.exchange(ec.ECDH(), Alice_private_key_secp192r1.public_key())
Bob_derived_key_secp192r1 = HKDF(algorithm=hashes.SHA256(), length=sizeSECP192R1, salt=None, info=b'', backend=default_backend()).derive(Bob_shared_key_secp192r1)

Alice_shared_key_secp192r1 = Alice_private_key_secp192r1.exchange(ec.ECDH(), Bob_private_key_secp192r1.public_key())
Alice_derived_key_secp192r1 = HKDF(algorithm=hashes.SHA256(), length=sizeSECP192R1, salt=None, info=b'', backend=default_backend()).derive(Alice_shared_key_secp192r1)

print("\nSECP192R1 Curve:")
print("Name of curve:", Bob_private_key_secp192r1.public_key().curve.name)
print(f"Generated key size: {sizeSECP192R1} bytes ({sizeSECP192R1*8} bits)")
print("Bob's derived key: ", binascii.b2a_hex(Bob_derived_key_secp192r1).decode())
print("Alice's derived key: ", binascii.b2a_hex(Alice_derived_key_secp192r1).decode())

# SECP521R1 Curve
sizeSECP521R1 = 521

Bob_private_key_secp521r1 = ec.generate_private_key(ec.SECP521R1(), default_backend())
Alice_private_key_secp521r1 = ec.generate_private_key(ec.SECP521R1(), default_backend())

Bob_shared_key_secp521r1 = Bob_private_key_secp521r1.exchange(ec.ECDH(), Alice_private_key_secp521r1.public_key())
Bob_derived_key_secp521r1 = HKDF(algorithm=hashes.SHA256(), length=sizeSECP521R1, salt=None, info=b'', backend=default_backend()).derive(Bob_shared_key_secp521r1)

Alice_shared_key_secp521r1 = Alice_private_key_secp521r1.exchange(ec.ECDH(), Bob_private_key_secp521r1.public_key())
Alice_derived_key_secp521r1 = HKDF(algorithm=hashes.SHA256(), length=sizeSECP521R1, salt=None, info=b'', backend=default_backend()).derive(Alice_shared_key_secp521r1)

print("\nSECP521R1 Curve:")
print("Name of curve:", Bob_private_key_secp521r1.public_key().curve.name)
print(f"Generated key size: {sizeSECP521R1} bytes ({sizeSECP521R1*8} bits)")
print("Bob's derived key: ", binascii.b2a_hex(Bob_derived_key_secp521r1).decode())
print("Alice's derived key: ", binascii.b2a_hex(Alice_derived_key_secp521r1).decode())
