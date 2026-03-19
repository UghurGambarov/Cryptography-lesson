import secrets

# Public parameters
p = 7919
g = 7

def prg(seed, n_bits):
    x = seed % p
    bits = ""
    for _ in range(n_bits):
        x = pow(g, x, p)
        bits += "1" if x > (p - 1) // 2 else "0"
    return bits

seed = secrets.randbelow(p - 2) + 2

print("Seed:", seed)
print("Output (64 bits):", prg(seed, 64))
print("Deterministic?", prg(seed, 64) == prg(seed, 64))
