import random

def XOR(msg,key):
    xor = ''
    aShift = decToBin(msg)
    bShift = decToBin(key)
    maxL = max(len(aShift), len(bShift))    
    for i,j in zip(aShift.zfill(maxL),bShift.zfill(maxL)):
        if i==j:
            xor +='0'
        else: xor += '1'
    return binToDec(xor)

def decToBin(a):
    if type(a) == str:
        a = ord(a)
    if a == 0: return '0'
    r =[]
    while a:
        r.append(str(a%2))
        a //= 2
    return "".join(r[::-1])

def binToDec(a):
    n = len(a)
    d = 0
    for i in a:
        d += 2**(n-1)*int(i)
        n -= 1
    return d

def encrypt(msg):
    key = random.randint(1,1000)
    cipherText = [XOR(c,key) for c in msg]
    return cipherText, key

def decrypt(cipterText, key):
    plainText = "".join([chr(XOR(c, key)) for c in cipterText])
    return plainText

msg = input("Enter message: ")
cipherT, key = encrypt(msg)
plain = decrypt(cipherT, key)

print("Message: ", msg)
print("Encrypted message: ", "".join([chr(i) for i in cipherT]))
print("Key: ", key)
print("Decrypted message: ", plain)