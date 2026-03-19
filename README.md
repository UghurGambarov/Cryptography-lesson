# Cryptography Implementations

10 cryptographic algorithms implemented in Python, from classical ciphers to modern public-key cryptography.

---

## Requirements

No dependencies needed except for one file:
```bash
pip install pycryptodome   # only for cpa_otp.py
```

---

## Files

### 1. `gcd.py` — Greatest Common Divisor
Repeatedly divides until remainder is 0. Foundation for everything else.
```bash
python gcd.py
```

---

### 2. `caesar.py` — Caesar Cipher
Shifts each letter by a fixed amount. `A→D, B→E, ...` with shift=3.
```bash
python caesar.py
```

---

### 3. `affine.py` — Affine Cipher
Generalizes Caesar using `E(x) = (a·x + b) mod 26`. Requires `gcd(a, 26) = 1`.
```bash
python affine.py
```

---

### 4. `otp.py` — One-Time Pad
XORs each character with a random key byte. Perfectly secure if the key is never reused.
```bash
python otp.py
```

---

### 5. `otp_prg.py` — OTP + PRG
Same as OTP but uses a short seed + SHA-256 to generate the keystream, so the key doesn't need to be as long as the message.
```bash
python otp_prg.py
```

---

### 6. `frequency_analysis.py` — Frequency Analysis Attack
Breaks Caesar cipher by finding the most common letter in the ciphertext and assuming it maps to `E`.
```bash
python frequency_analysis.py
```
> Works best on long texts (100+ characters).

---

### 7. `cpa_otp.py` — CPA-Secure OTP (AES-CTR)
Uses AES + a random nonce to ensure the same message encrypts differently every time (CPA security).
```bash
pip install pycryptodome
python cpa_otp.py
```

---

### 8. `extended_gcd.py` — Extended Euclidean Algorithm
Finds `x, y` such that `a·x + b·y = gcd(a, b)`. Used to compute modular inverses needed by RSA and Affine.
```bash
python extended_gcd.py
```

---

### 9. `rsa.py` — RSA Encryption
Public-key encryption. Encrypts with `c = m^e mod n`, decrypts with `m = c^d mod n`.
```bash
python rsa.py
```

---

### 10. `diffie_hellman.py` — Diffie-Hellman Key Exchange
Two parties agree on a shared secret over a public channel without ever sending the secret itself.
```bash
python diffie_hellman.py
```

---

### 11. `prg_dl.py` — PRG Based on Discrete Log
Generates pseudorandom bits using `x = g^x mod p`. Security reduces to the hardness of the discrete logarithm problem.
```bash
python prg_dl.py
```
