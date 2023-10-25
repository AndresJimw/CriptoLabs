def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi_n):
    d = 0
    x1, x2, y1, y2 = 1, 0, 0, 1
    temp_phi_n = phi_n
    
    while e > 0:
        q = temp_phi_n // e
        temp_phi_n, e = e, temp_phi_n % e
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2
        
    if temp_phi_n == 1:
        d = y1 % phi_n
    
    return d

# Parámetros RSA de Alice
p = 5
q = 11
e = 17

# Calcular n y φ(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Calcular clave privada de Alice (d)
d = mod_inverse(e, phi_n)

# Mensaje a cifrar por Bob
x = 4

# Cifrado del mensaje por Bob
C = pow(x, e, n)

# Descifrado del mensaje por Alice
decrypted_text = pow(C, d, n)

# Mostrar resultados
print("Clave pública de Alice (e, n):", (e, n))
print("Clave privada de Alice (d, n):", (d, n))
print("Texto cifrado por Bob (C):", C)
print("Texto descifrado por Alice:", decrypted_text)




""" 
Bob wants to send an encrypted message to Alice. She first
computes her RSA parameters (p = 5, q = 11 and e = 17).
Alice then sends Bob her public key. Bob encrypts the
message (x = 4) and sends the ciphertext C to Alice. She
decrypts x using her private key. Compute private key,
public key, ciphertext and decrypted text.

Funciones gcd y mod_inverse:

gcd(a, b): Calcula el máximo común divisor.
mod_inverse(e, phi_n): Calcula el inverso modular de e en relación con phi_n.

Cálculos de Claves y Cifrado:

Se calculan las claves pública y privada de Alice.
Se cifra el mensaje x=4 usando la clave pública de Alice.
Descifrado:

Se descifra el texto cifrado C usando la clave privada de Alice.
Mostrar Resultados:

Se muestran las claves y los mensajes cifrado y descifrado. """