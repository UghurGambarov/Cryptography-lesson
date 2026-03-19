def caesar_encrypt(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            x = ord(c.upper()) - 65
            enc = (x + shift) % 26
            result += chr(enc + 65)
        else:
            result += c
    return result

def caesar_decrypt(cipher, shift):
    return caesar_encrypt(cipher, -shift)

shift = 3

msg    = input("Enter message: ")
cipher = caesar_encrypt(msg, shift)
plain  = caesar_decrypt(cipher, shift)

print("Encrypted:", cipher)
print("Decrypted:", plain)
