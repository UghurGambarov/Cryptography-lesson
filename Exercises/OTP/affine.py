def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("No modular inverse exists!")

def affine_encrypt(text, a, b):
    result = ""
    for c in text:
        if c.isalpha():
            x = ord(c.upper()) - 65
            enc = (a * x + b) % 26
            result += chr(enc + 65)
        else: result += c
    return result

def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    for c in cipher:
        if c.isalpha():
            y = ord(c.upper()) - 65
            dec = (a_inv * (y - b)) % 26
            result += chr(dec + 65)
        else: result += c
    return result

a = 7
b = 10

msg = input("Enter message: ")
cipher = affine_encrypt(msg, a, b)
plain  = affine_decrypt(cipher, a, b)

print("Encrypted:", cipher)
print("Decrypted:", plain)
