def caesar_encrypt(plaintext: str, shift: int) -> str:
    def shift_char(c):
        if 'A' <= c <= 'Z':
            return chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        if 'a' <= c <= 'z':
            return chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        return c
    return ''.join(shift_char(c) for c in plaintext)

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    return caesar_encrypt(ciphertext, -shift)

if __name__ == "__main__":
    text = "Attack at dawn!"
    shift = 3
    encrypted = caesar_encrypt(text, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print("Plaintext: ", text)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted)

