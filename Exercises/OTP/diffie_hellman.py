import random

# Public parameters
p = 23
g = 5

# Private keys
a = random.randint(2, p - 2)   # Alice
b = random.randint(2, p - 2)   # Bob

# Public keys
A = pow(g, a, p)   # Alice sends this
B = pow(g, b, p)   # Bob sends this

# Shared secrets
s_alice = pow(B, a, p)
s_bob   = pow(A, b, p)

print(f"Public params: p={p}, g={g}")
print(f"Alice private: {a}  =>  public: {A}")
print(f"Bob   private: {b}  =>  public: {B}")
print(f"Alice shared secret: {s_alice}")
print(f"Bob   shared secret: {s_bob}")
print(f"Match: {s_alice == s_bob}")
