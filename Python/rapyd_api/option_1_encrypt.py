from cryptography.fernet import Fernet
import os

def main():
    create_key()
    read_key()
    choice = input('would you like to decrypt (d) or encrypt (e)?: ')
    if choice == 'e':
        encrypt()
    else:
        decrypt()

def create_key():
    file_exists = os.path.isfile('yek.txt')
    try:
        file_empty = os.stat('yek.txt').st_size == 0   
    except FileNotFoundError:
        file_empty = False

    if (file_exists == False):
        key = Fernet.generate_key()
        with open('yek.txt', 'wb') as file:
            file.write(key)

    if (file_empty == True):
        key = Fernet.generate_key()
        with open('yek.txt', 'wb') as file:
            file.write(key)

def read_key():
    with open('yek.txt', 'rb') as file:
        key = file.read()
    return key

def encrypt():
    pass
def decrypt():
    pass

if __name__ == '__main__':
    main()