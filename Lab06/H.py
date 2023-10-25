# Parámetros del sistema
p = 61
alpha = 18
a = 11
b = 22
c = 33
ID_A = 1
ID_B = 2
ID_C = 3

p_prime = 467
alpha_prime = 2
d_prime = 127
kE_A = 213
kE_B = 215
kE_C = 217

# Cálculo de xi para Certificados
xi_A = 4 * b + ID_A
xi_B = 4 * c + ID_B
xi_C = 4 * a + ID_C

# Firma para Certificado de Alice
r_A = pow(alpha_prime, kE_A, p_prime)
s_A = (xi_A - 2 * a * kE_A) * pow(d_prime, -1, p_prime) % p_prime

# Firma para Certificado de Bob
r_B = pow(alpha_prime, kE_B, p_prime)
s_B = (xi_B - 2 * b * kE_B) * pow(d_prime, -1, p_prime) % p_prime

# Firma para Certificado de Charley
r_C = pow(alpha_prime, kE_C, p_prime)
s_C = (xi_C - 2 * c * kE_C) * pow(d_prime, -1, p_prime) % p_prime

# Verificación de Certificados
verification_A = (pow(r_A, s_A, p_prime) * pow(alpha_prime, xi_A, p_prime)) % p_prime
verification_B = (pow(r_B, s_B, p_prime) * pow(alpha_prime, xi_B, p_prime)) % p_prime
verification_C = (pow(r_C, s_C, p_prime) * pow(alpha_prime, xi_C, p_prime)) % p_prime

# Cálculo de Claves de Sesión
k_AB = pow(r_B, a * ID_B, p_prime)
k_AC = pow(r_C, a * ID_C, p_prime)
k_BC = pow(r_C, b * ID_C, p_prime)

# Resultados
print("Certificado de Alice (CertA):")
print("Firma (r_A, s_A):", r_A, s_A)
print("Verificación Aprobada:", verification_A == r_A)

print("\nCertificado de Bob (CertB):")
print("Firma (r_B, s_B):", r_B, s_B)
print("Verificación Aprobada:", verification_B == r_B)

print("\nCertificado de Charley (CertC):")
print("Firma (r_C, s_C):", r_C, s_C)
print("Verificación Aprobada:", verification_C == r_C)

print("\nClaves de Sesión:")
print("k_AB:", k_AB)
print("k_AC:", k_AC)
print("k_BC:", k_BC)
