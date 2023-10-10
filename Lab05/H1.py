def calculate_public_key(alpha, private_key, prime):
    return pow(alpha, private_key, prime)

def calculate_shared_key(public_key, private_key, prime):
    return pow(public_key, private_key, prime)

def diffie_hellman(alpha, a, b, prime):
    alice_public_key = calculate_public_key(alpha, a, prime)
    bob_public_key = calculate_public_key(alpha, b, prime)
    
    alice_shared_key = calculate_shared_key(bob_public_key, a, prime)
    bob_shared_key = calculate_shared_key(alice_public_key, b, prime)
    
    return alice_public_key, bob_public_key, alice_shared_key, bob_shared_key

# Valores dados
alpha = 2
p = 467

# Caso 1: a = 3, b = 5
a1, b1, shared_key_a1, shared_key_b1 = diffie_hellman(alpha, 3, 5, p)

# Caso 2: a = 400, b = 134
a2, b2, shared_key_a2, shared_key_b2 = diffie_hellman(alpha, 400, 134, p)

# Caso 3: a = 228, b = 57
a3, b3, shared_key_a3, shared_key_b3 = diffie_hellman(alpha, 228, 57, p)

# Resultados
print("Caso 1:")
print("Clave pública de Alice:", a1)
print("Clave pública de Bob:", b1)
print("Clave compartida de Alice:", shared_key_a1)
print("Clave compartida de Bob:", shared_key_b1)
print()

print("Caso 2:")
print("Clave pública de Alice:", a2)
print("Clave pública de Bob:", b2)
print("Clave compartida de Alice:", shared_key_a2)
print("Clave compartida de Bob:", shared_key_b2)
print()

print("Caso 3:")
print("Clave pública de Alice:", a3)
print("Clave pública de Bob:", b3)
print("Clave compartida de Alice:", shared_key_a3)
print("Clave compartida de Bob:", shared_key_b3)
