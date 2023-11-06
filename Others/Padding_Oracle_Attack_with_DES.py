#This code is for padding oracle attack using DES algorithms
#You can use with command like "python3 Padding_Oracle_Attack_with_DES.py argument0 argument1

import sys
from Crypto.Cipher import DES

def decrypt_des(ciphertext_hex, key_hex):
    ciphertext = bytes.fromhex(ciphertext_hex)
    key = bytes.fromhex(key_hex)
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 app.py <c0> <c1>")
        sys.exit(1)

    c0_hex = sys.argv[1]
    c1_hex = sys.argv[2]

    plaintext = decrypt_des(c0_hex, c1_hex)

    print(f"C0: {c0_hex}, C1: {c1_hex} -> {plaintext.decode('utf-8')}")
