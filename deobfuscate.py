# This code was written by xZin0vich I take all credits.

import sys

def deobfuscate(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()

    encrypted_data_line = lines[0].strip()
    encryption_key_line = lines[1].strip()

    encrypted_data = encrypted_data_line.split(" =\"")[1][:-1]
    encryption_key = encryption_key_line.split(" = \"")[1][:-1]

    decrypted_data = ""
    for i in range(len(encrypted_data)):
        current_char = encrypted_data[i]
        current_key = encryption_key[i % len(encryption_key)]
        decrypted_data += chr(ord(current_char) ^ ord(current_key))

    return decrypted_data

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python deobfuscate.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    decrypted_data = deobfuscate(input_file)

    with open(output_file, "w") as f:
        f.write(decrypted_data)

    print(f"Deobfuscated code has been written to {output_file}")
