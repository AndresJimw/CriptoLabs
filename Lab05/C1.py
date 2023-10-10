
g = 3
p = 11

for i in range(1,13):
    x = i
    fx = pow(g,x) % p
    print(f"f(x{i}): {fx}")
    