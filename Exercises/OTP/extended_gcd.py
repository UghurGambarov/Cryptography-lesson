def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("No inverse exists!")
    return x % m

a = int(input("Enter a: "))
b = int(input("Enter b: "))

g, x, y = extended_gcd(a, b)
print(f"GCD: {g}")
print(f"Bezout coefficients: x={x}, y={y}")
print(f"Check: {a}*{x} + {b}*{y} = {a*x + b*y}")

m = int(input("Find inverse of a mod m, enter m: "))
print(f"Inverse of {a} mod {m}: {mod_inverse(a, m)}")
