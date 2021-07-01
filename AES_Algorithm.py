import pathlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii


def encrypt_file(key, filename):
    try:
        key = key.encode("utf-8") # convert key to binary 
        cipher = AES.new(key, AES.MODE_CBC) # create AES object  with  block cipher mode = (cipher-block chaining)
        if pathlib.Path(filename).exists():
            with open(filename, "r") as file:
                plan_text = file.read().encode("utf-8")
                file.close()
            with open(f"{filename.split('.')[0]}.encrypted", "w") as encryptedFile:
                ciphertext = cipher.encrypt(pad(plan_text, AES.block_size)) # encrypt text with padding function
                encryptedFile.write(binascii.b2a_base64(cipher.iv).decode("utf-8")) # write initialization vector 
                encryptedFile.write(binascii.b2a_base64(ciphertext).decode("utf-8"))# write plan text
                encryptedFile.close()
                # print(binascii.hexlify(ciphertext))
            print(f"Done! File {filename} is encrypted using AES-192\nOutput file is {filename.split('.')[0]}.encrypted")
        else:
            print(f"File name : {filename} Not Exist\nEnter Exist File Pleas")
    except Exception as e:
        print(f" There is issue ??? {e}"+"\n"*3)
        print('-' * 50)


def decrypt_file(key, filename, directory=''):
    try:
        key = key.encode("utf-8")
        if pathlib.Path(filename+".encrypted").exists():
            with open(filename+".encrypted", "r")as decrypt:
                iv = binascii.a2b_base64(decrypt.readline()) # read initialization vector 
                ciphertext = binascii.a2b_base64(decrypt.read())  # read encrypt text 
                decrypt.close()
            cipher = AES.new(key, AES.MODE_CBC, iv) # create AES object
            plan_text = unpad(cipher.decrypt(ciphertext), AES.block_size).decode() # decrypt text filr useing AES
            with open(directory.join(filename)+".decrypted", "w") as encryptedFile:
                encryptedFile.write(plan_text) # read plan text
                encryptedFile.close()
            # print(plan_text.decode())
            print(f"Done! File {filename} is decrypted using AES-192\nOutput file is {filename}.decrypted")
        else:
            print(f"File name : {filename} Not Exist\nEnter Exist File Pleas")
    except Exception as e:
        print(f" There is issue ??? {e}"+"\n"*3)
        print('-' * 50)
