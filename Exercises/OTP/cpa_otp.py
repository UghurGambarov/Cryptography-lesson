import secrets
from Crypto.Cipher import AES

def encrypt(msg, key):
    nonce = secrets.token_bytes(16)
    cipher = AES.new(key, AES.MODE_CTR, nonce=b"", initial_value=nonce)
    ciphertext = cipher.encrypt(msg)
    return nonce, ciphertext

def decrypt(nonce, ciphertext, key):
    cipher = AES.new(key, AES.MODE_CTR, nonce=b"", initial_value=nonce)
    return cipher.decrypt(ciphertext)

key = secrets.token_bytes(16)
msg = input("Enter message: ").encode()

nonce, cipher = encrypt(msg, key)
plain = decrypt(nonce, cipher, key)

print("Key:       ", key.hex())
print("Nonce:     ", nonce.hex())
print("Encrypted: ", cipher.hex())
print("Decrypted: ", plain.decode())
