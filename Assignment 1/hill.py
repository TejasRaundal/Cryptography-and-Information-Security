import numpy as np

def mod_inverse(a, m):
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for {a} mod {m}")

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numbers_to_text(numbers):
    return ''.join(chr(num % 26 + ord('A')) for num in numbers)

def pad_text(text, block_size):
    text = ''.join(filter(str.isalpha, text.upper()))
    while len(text) % block_size != 0:
        text += 'X'
    return text

def hill_encryption(plaintext, key):
    n = key.shape[0]
    plaintext = pad_text(plaintext, n)
    nums = text_to_numbers(plaintext)
    ciphertext = ''
    for i in range(0, len(nums), n):
        block = np.array(nums[i:i+n])
        result = np.dot(key, block) % 26
        ciphertext += numbers_to_text(result)
    return ciphertext

# def hill_decryption(ciphertext, key):
#     n = key.shape[0]
#     nums = text_to_numbers(ciphertext)
#     key_inv = mod_inverse(key, 26)
#     plaintext = ''
#     for i in range(0, len(nums), n):
#         block = np.array(nums[i:i+n])
#         result = np.dot(key_inv, block) % 26
#         plaintext += numbers_to_text(result)
#     return plaintext

def create_key_matrix(key_str):
    key_str = key_str.upper()
    key_nums = text_to_numbers(key_str)
    length = len(key_nums)
    size = int(length**0.5)
    if size * size != length:
        raise ValueError(f"Key length is {length}, which is not a perfect square:")
    return np.array(key_nums).reshape(size, size)


plaintext = input("Enter plaintext to encrypt: ")

key = input("Enter key: ")
matrix = create_key_matrix(key)

encrypted = hill_encryption(plaintext, matrix)
print("Encrypted text:", encrypted)

# decrypted = hill_decryption(plaintext, matrix)
# print("Decrypted text:", decrypted)