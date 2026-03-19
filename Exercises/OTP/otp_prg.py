import secrets
import hashlib

def prg(seed, length):
    output = b""
    counter = 0
    while len(output) < length:
        output += hashlib.sha256(seed + counter.to_bytes(4, "big")).digest()
        counter += 1
    return output[:length]

def encrypt(msg, seed):
    key = prg(seed, len(msg))
    cipher = []
    for m, k in zip(msg, key):
        cipher.append(m ^ k)
    return bytes(cipher)

msg  = input("Enter message: ").encode()
seed = secrets.token_bytes(16)

cipher = encrypt(msg, seed)
plain  = encrypt(cipher, seed)

print("Seed:      ", seed.hex())
print("Encrypted: ", cipher.hex())
print("Decrypted: ", plain.decode())
