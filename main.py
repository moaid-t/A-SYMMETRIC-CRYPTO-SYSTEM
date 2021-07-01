import os
import AES_Algorithm
import DES_Algorithm


while True:
    try:
        print("\t"*3+"A SYMMETRIC CRYPTO SYSTEM")
        print('''==========================================================================
        MAIN MENU
        ----------------------
        1.Encrypt
        2.Decrypt
        3.Exit
        ----------------------''')
        cryptography = int(input("Enter your choice: "))
        if cryptography == 1 or cryptography == 2:
            print("(1) File (2) Folder")
            f_choice = int(input("Enter your choice: "))
            algorithm = input("Algorithm (AES, DES): ").strip()
            # Start Encrypt
            if cryptography == 1:
                # Start File Encrypt
                if f_choice == 1:
                    fileName = input("Name: ").strip()
                    key = input("Key : ").strip()
                    if algorithm == "AES":
                        AES_Algorithm.encrypt_file(key, fileName)
                    elif algorithm == "DES":
                        DES_Algorithm.encrypt_file(key, fileName)
                    else:
                        print("Enter Exist Algorithm")
                    print('-' * 50)
                # End File Encrypt
                # Start Folder Encrypt
                elif f_choice == 2:
                    path = input("Enter The Foldr Path: /")  # 'container001' or 'container002'
                    key = input("Key : ").strip()
                    if algorithm == "AES":
                        # Save all files in list
                        text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
                        # For Each file make AES encrypt
                        for f in text_files:
                            AES_Algorithm.encrypt_file(key, path+'/'+f)
                    elif algorithm == "DES":
                        text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
                        for f in text_files:
                            DES_Algorithm.encrypt_file(key, path + '/' + f)
                    else:
                        print("Enter Exist Algorithm")
                    print('-' * 50)
                # End Folder Encrypt
            # Close Encrypt
            # Start Decrypt
            elif cryptography == 2:
                # Start File Decrypt
                if f_choice == 1:
                    fileName = input("Name: ").strip()
                    key = input("Key : ")
                    if algorithm == "AES":
                        AES_Algorithm.decrypt_file(key, fileName)
                    elif algorithm == "DES":
                        DES_Algorithm.decrypt_file(key, fileName)
                    else:
                        print("Enter Exist Algorithm")
                    print('-' * 50)
                # close File Decrypt
                # Start folder Decrypt
                elif f_choice == 2:
                    path = input("Enter The Foldr Path: /")  # 'container001' or 'container002'
                    key = input("Key : ")
                    if algorithm == "AES":
                        text_files = [f.split('.')[0] for f in os.listdir(path) if f.endswith('.encrypted')]
                        for f in text_files:
                            AES_Algorithm.decrypt_file(key, path + '/' + f)
                    elif algorithm == "DES":
                        text_files = [f.split('.')[0] for f in os.listdir(path) if f.endswith('.encrypted')]
                        for f in text_files:
                            DES_Algorithm.decrypt_file(key, path + '/' + f)
                    else:
                        print("Enter Exist Algorithm")
                    print('-' * 50)
                # end folder Decrypt
            # End Decrypt
        elif cryptography == 3:
            print("Exit Don")
            print('-' * 50)
            break
        else:
            print("Enter Exist choice")
            print('-' * 50)
    except Exception as e:
        print(f" There is issue ??? {e}"+"\n"*3)
        print('-' * 50)
