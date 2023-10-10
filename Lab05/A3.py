
g = 5
N = 23
x = 3
y = 4
A = pow(g,x) % N
B = pow(g,y) % N

print("A value: ", A)
print("B value: ", B)

# Calculate the shared key
skeybyB = pow(B,x) % N
skeybyA = pow(A,y) % N

print("Shared key by B value: ", skeybyB)
print("Shared key by A value: ", skeybyA)
