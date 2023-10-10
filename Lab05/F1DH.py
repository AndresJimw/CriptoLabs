def baby_step_giant_step(g, p, A_or_B):
    # Baby-step
    baby_steps = {}
    m = int(p ** 0.5)
    for j in range(m):
        baby_steps[pow(g, j, p)] = j

    # Giant-step
    giant_step_multiplier = pow(g, -m, p)
    giant_step_value = A_or_B
    for k in range(m + 1):
        if giant_step_value in baby_steps:
            baby_step_index = baby_steps[giant_step_value]
            return m * k + baby_step_index
        giant_step_value = (giant_step_value * giant_step_multiplier) % p

    return None  # No se encontró a o b

g = 5
p = 97
A = 35  # Alice
B = 80  # Bob

a_found = baby_step_giant_step(g, p, A)
b_found = baby_step_giant_step(g, p, B)

print("Secret value a found:", a_found)
print("Secret value b found:", b_found)