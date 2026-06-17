from pathlib import Path

def shift_left(b):
    return ((b << 2) | (b >> 6)) & 255

def shift_right(b):
    return ((b >> 2) | (b << 6)) & 255

def main():
    key = 85
    
    path_in = Path(__file__).parent / "resource" / "original.txt"
    path_enc = Path(__file__).parent / "resource" / "encrypted.bin"
    path_dec = Path(__file__).parent / "resource" / "decrypted.txt"
    
    with open(path_in, "rb") as f:
        original = f.read()
    
    encrypted = []
    for b in original:
        encrypted.append(shift_left(b) ^ key)
    
    with open(path_enc, "wb") as f:
        f.write(bytes(encrypted))
    
    decrypted = []
    for b in encrypted:
        decrypted.append(shift_right(b ^ key))
    
    with open(path_dec, "wb") as f:
        f.write(bytes(decrypted))
    
    print("Исходные данные:", original)
    print("Зашифрованные:", bytes(encrypted))
    print("Расшифрованные:", bytes(decrypted))

if __name__ == "__main__":
    main()