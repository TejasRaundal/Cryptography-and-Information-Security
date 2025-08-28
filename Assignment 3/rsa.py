from math import gcd

def rsa():
    message = input("Enter plaintext (string): ")

    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if gcd(phi, e) != 1:
        e = 3  # fallback

    # modular inverse of e mod phi
    d = pow(e, -1, phi)

    print(f"\nPublic key (e, n): ({e}, {n})")
    print(f"Private key (d, n): ({d}, {n})")
    print("Plaintext :", message)

    # Encrypt each character
    ciphertexts = [pow(ord(ch), e, n) for ch in message]
    print("Ciphertext:", " ".join(map(str, ciphertexts)))

    # Decrypt each character
    decrypted = "".join(chr(pow(c, d, n)) for c in ciphertexts)
    print("Decrypted :", decrypted)


if __name__ == "__main__":
    rsa()
