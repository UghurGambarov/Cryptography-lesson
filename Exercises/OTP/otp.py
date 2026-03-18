import secrets

def encrypt(msg, key):
    cipher = []
    for m, k in zip(msg, key):
        m_bin = decToBin8(ord(m))
        k_bin = decToBin8(k)
        x_bin = xorBin(m_bin, k_bin)
        cipher.append(binToDec(x_bin))
    return bytes(cipher)

def binToDec(a): 
    n = len(a) 
    d = 0 
    for i in a: 
        d += 2**(n-1)*int(i) 
        n -= 1 
    return d

def decToBin8(n):
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n //= 2
    return b.zfill(8)

def xorBin(a, b):
    r = ""
    for i, j in zip(a, b):
        if i == j: r += "0"
        else: r += "1"
    return r

msg = input("Enter your message: ")
key = secrets.token_bytes(len(msg))

cipher = encrypt(msg, key)
plain  = encrypt(cipher.decode("latin1"), key)

print("Key:", key)
print("Cipher:", cipher)
print("Decrypted:", plain)
