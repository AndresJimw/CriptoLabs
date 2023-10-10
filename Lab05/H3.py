# Función para calcular la clave compartida usando Diffie-Hellman
def diffie_hellman(alpha, a, b, p):
    alice_shared_key = pow(alpha, a * b, p)
    bob_shared_key = pow(alpha, b, p)
    return alice_shared_key, bob_shared_key

p = 467
alpha = 4

# Case 1: a = 400, b = 134
a1 = 400
b1 = 134
shared_key_a1, shared_key_b1 = diffie_hellman(alpha, a1, b1, p)

# Case 2: a = 167, b = 134
a2 = 167
b2 = 134
shared_key_a2, shared_key_b2 = diffie_hellman(alpha, a2, b2, p)

print("Case 1 - Shared Key Alice:", shared_key_a1)
print("Case 1 - Shared Key Bob:", shared_key_b1)

print("Case 2 - Shared Key Alice:", shared_key_a2)
print("Case 2 - Shared Key Bob:", shared_key_b2)