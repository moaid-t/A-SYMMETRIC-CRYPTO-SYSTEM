import pathlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii


def encrypt_file(key, filename):
    try:
        key = key.encode("utf-8")
        cipher = AES.new(key, AES.MODE_CBC)
        if pathlib.Path(filename).exists():
            with open(filename, "r") as file:
                plan_text = file.read().encode("utf-8")
                file.close()
            with open(f"{filename.split('.')[0]}.encrypted", "w") as encryptedFile:
                ciphertext = cipher.encrypt(pad(plan_text, AES.block_size))
                encryptedFile.write(binascii.b2a_base64(cipher.iv).decode("utf-8"))
                encryptedFile.write(binascii.b2a_base64(ciphertext).decode("utf-8"))
                encryptedFile.close()
                # print(binascii.hexlify(ciphertext))
            print(f"Done! File {filename} is encrypted using AES-192\nOutput file is {filename.split('.')[0]}.encrypted")
        else:
            print(f"File name : {filename} Not Exist\nEnter Exist File Pleas")
    except Exception as e:
        print(f" Exception is ==? {e}")
        print("Enter The Correct Key please")


def decrypt_file(key, filename, directory=''):
    try:
        key = key.encode("utf-8")
        if pathlib.Path(filename+".encrypted").exists():
            with open(filename+".encrypted", "r")as decrypt:
                iv = binascii.a2b_base64(decrypt.readline())
                ciphertext = binascii.a2b_base64(decrypt.read())
                decrypt.close()
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plan_text = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
            with open(directory.join(filename)+".decrypted", "w") as encryptedFile:
                encryptedFile.write(plan_text)
                encryptedFile.close()
            # print(plan_text.decode())
            print(f"Done! File {filename} is decrypted using AES-192\nOutput file is {filename}.decrypted")
        else:
            # print(f"File name : {filename} Not Exist\nEnter Exist File Pleas")
            print(f"File name : {filename} Not Exist\nEnter Exist File Pleas")
    except Exception as e:
        print(f" Exception is ==? {e}")
        print("Enter The Correct Key please")
