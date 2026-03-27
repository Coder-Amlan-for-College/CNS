def prepare_key(key, n):
    return (key * (n // len(key) + 1))[:n]

def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    
    key = prepare_key(key, len(plain_text))
    
    cipher_text = ""
    for p, k in zip(plain_text, key):
        c = chr((ord(p) - ord('A') + ord(k) - ord('A')) % 26 + ord('A'))
        cipher_text += c
    
    return cipher_text

# Input
plain_text = input("Plain Text: ").strip()
key = input("Key: ").strip()

print("Cipher Text:", vigenere_encrypt(plain_text, key))