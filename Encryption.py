from cryptography.fernet import Fernet
import sys

"""
Made by: IsaacNewTom
Prerequisites:
    Download "cryptography" package
    Make sure you create a keyfile in the same directory as this file!
"""


# this function encrypts a string
def EncryptString(str):
    # open key file
    try:
        with open("Hacktoberfest2022\\keyfile.key", 'r') as keyfile:
            key = keyfile.read()
    except OSError:
        print("Could not open/read keyfile")
        sys.exit()

    # init fernet object
    fernet = Fernet(key)

    return fernet.encrypt(bytes(str, 'utf-8')).decode("utf-8")

# this function decrypts a string
def DecryptString(str):
    # open key file
    try:
        with open("Hacktoberfest2022\\keyfile.key", 'r') as keyfile:
            key = keyfile.read()
    except OSError:
        print("Could not open/read keyfile")
        sys.exit()

    # init fernet object
    fernet = Fernet(key)

    return fernet.decrypt(bytes(str, 'utf-8')).decode("utf-8")


def main():
    plain_text = "Secret message!"
    encrypted_string = EncryptString(plain_text)
    decrypted_string = DecryptString(encrypted_string)

    print(f"The encrypted message is: {encrypted_string}\nThe decrypted message is: {decrypted_string}")

if __name__ == '__main__':
    main()