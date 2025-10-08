def _letter_index(c):
    return ord(c) - ord('A') if 'A' <= c <= 'Z' else ord(c) - ord('a')

def vigenere_encrypt(plaintext: str, key: str) -> str:
    key_letters = [k.upper() for k in key if k.isalpha()]
    if not key_letters:
        raise ValueError("Key must contain alphabetic characters.")
    out = []
    ki = 0
    for ch in plaintext:
        if ch.isalpha():
            k_shift = ord(key_letters[ki % len(key_letters)]) - ord('A')
            if ch.isupper():
                out.append(chr((ord(ch) - ord('A') + k_shift) % 26 + ord('A')))
            else:
                out.append(chr((ord(ch) - ord('a') + k_shift) % 26 + ord('a')))
            ki += 1
        else:
            out.append(ch)
    return ''.join(out)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    key_letters = [k.upper() for k in key if k.isalpha()]
    if not key_letters:
        raise ValueError("Key must contain alphabetic characters.")
    out = []
    ki = 0
    for ch in ciphertext:
        if ch.isalpha():
            k_shift = ord(key_letters[ki % len(key_letters)]) - ord('A')
            if ch.isupper():
                out.append(chr((ord(ch) - ord('A') - k_shift) % 26 + ord('A')))
            else:
                out.append(chr((ord(ch) - ord('a') - k_shift) % 26 + ord('a')))
            ki += 1
        else:
            out.append(ch)
    return ''.join(out)

if __name__ == "__main__":
    text = "Attack at dawn!"
    key = "LEMON"
    encrypted = vigenere_encrypt(text, key)
    decrypted = vigenere_decrypt(encrypted, key)

    print("Plaintext: ", text)
    print("Key:       ", key)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted)

