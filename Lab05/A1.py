
g = 2879 
N = 9929
x = 6
y = 9
A = pow(g,y) % N
B = pow(g,x) % N

print("Alice's A value: ", A)
print("Bob's B value: ", B)

# Calculate the shared key
keyB = pow(A,x) % N
keyA = pow(B,y) % N

print("Bob's value: ", keyB)
print("Alice's value: ", keyA)