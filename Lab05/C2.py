import sys 

p1 = 11
p2 = 41
p3 = 199
p4 = 2

def getG(p):
    valid_generators = []
    for x in range(1, p): 
        rand = x
        exp = 1
        next_val = rand % p

        while next_val != 1:
            next_val = (next_val * rand) % p 
            exp = exp + 1
            if exp == p - 1: 
                valid_generators.append(rand)
    return valid_generators

print(f'Selecting G for {p1}:', end=' ')
print(getG(p1))

print(f'Selecting G for {p2}:', end=' ')
print(getG(p2))

print(f'Selecting G for {p3}:', end=' ')
print(getG(p3))

print(f'Selecting G for {p4}:', end=' ')
print(getG(p4))
