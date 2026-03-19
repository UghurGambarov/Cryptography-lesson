import random

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def generate_prime(bits=8):
    while True:
        n = random.getrandbits(bits) | 1
        if is_prime(n):
            return n

def extended_gcd(a, b):
    if b == 0: return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def mod_inverse(e, phi):
    _, x, _ = extended_gcd(e, phi)
    return x % phi

# Key generation
p = generate_prime(8)
q = generate_prime(8)
while q == p:
    q = generate_prime(8)

n   = p * q
phi = (p - 1) * (q - 1)
e   = 65537 if 65537 < phi and extended_gcd(65537, phi)[0] == 1 else 3
d   = mod_inverse(e, phi)

print(f"p={p}, q={q}, n={n}, e={e}, d={d}")

msg = int(input("Enter a number to encrypt (must be < n): "))

cipher = pow(msg, e, n)
plain  = pow(cipher, d, n)

print("Encrypted:", cipher)
print("Decrypted:", plain)
