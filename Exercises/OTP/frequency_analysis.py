def get_frequencies(text):
    counts = {}
    total = 0
    for c in text.upper():
        if c.isalpha():
            counts[c] = counts.get(c, 0) + 1
            total += 1
    for c in counts:
        counts[c] = round(counts[c] / total * 100, 2)
    return counts

def crack_caesar(cipher):
    freq = get_frequencies(cipher)
    most_common = max(freq, key=freq.get)
    shift = (ord(most_common) - ord('E')) % 26

    result = ""
    for c in cipher:
        if c.isalpha():
            x = ord(c.upper()) - 65
            result += chr((x - shift) % 26 + 65)
        else:
            result += c
    return shift, result

cipher = input("Enter ciphertext: ")

print("Letter frequencies:", get_frequencies(cipher))
shift, plain = crack_caesar(cipher)
print("Guessed shift:", shift)
print("Decrypted:", plain)
