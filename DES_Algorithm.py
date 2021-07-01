import pathlib
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def encrypt_file(key, filename):
    try:
        key = key.encode("utf-8")
        name = filename.split('.')[0]
        cipher = DES.new(key, DES.MODE_ECB)
        if pathlib.Path(filename).exists():
            with open(filename, "r") as file:
                plan_text = file.read().encode("utf-8")
                file.close()
            with open(f"{name}.encrypted", "w") as encryptedFile:
                ciphertext = cipher.encrypt(pad(plan_text, DES.block_size))
                encryptedFile.write(binascii.b2a_base64(ciphertext).decode("utf-8"))
                encryptedFile.close()
            # print(binascii.hexlify(ciphertext))
            print(f"Done! File {name} is encrypted using DRS-64\nOutput file is {name}.encrypted")
        else:
            print(f"File name : {filename} Not Exist\nEnter Exist File Pleas")
    except Exception as e:
        print(f" Exception is ==? {e}")
        print("Enter The Correct Key please")


def decrypt_file(key, filename):
    try:
        key = key.encode("utf-8")
        if pathlib.Path(filename + ".encrypted").exists():
            with open(filename + ".encrypted", "r") as decrypt:
                ciphertext = decrypt.read()
                ciphertext = binascii.a2b_base64(ciphertext)
                decrypt.close()
            cipher = DES.new(key, DES.MODE_ECB)
            plan_text = unpad(cipher.decrypt(ciphertext), DES.block_size)
            with open(f"{filename}.decrypted", "w") as encryptedFile:
                encryptedFile.write(plan_text.decode("utf-8"))
                encryptedFile.close()
            # print(plan_text.decode())
            print(f"Done! File {filename} is decrypted using DES\nOutput file is {filename}.decrypted")
        else:
            print(f"File name : {filename} Not Exist\nEnter Exist File Pleas")
    except Exception as e:
        print(f" Exception is ==? {e}")
        print("Enter The Correct Key please")
