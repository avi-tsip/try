import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def main():
    user_choice = input('Would you like to encrypt (e) or decrypt (d)?: ')
    if user_choice == 'e':
        encrypt()
    else:
        decrypt()

def generate_key():    
    # Ask the user for a password
    user_password = input('Type password: ')
    password = user_password.encode()

    # Key prerequisites
    salt = b'j27gzj4zobdn{kz7m\jaojo\4lkg0}2xa[6ew6[80memhuv44o28jjmcty9o0fmy0g7bcvjnok7j53jpnoevym'
    kdf = PBKDF2HMAC (algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000,backend=default_backend())

    # Create key
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

print(generate_key)


def encrypt():
    with open('keys.txt', 'rb') as file:
        data = file.read()
    
    fer_obj = Fernet(generate_key())
    encrypted = fer_obj.encrypt(data)

    with open('encrypted.txt', 'wb') as file:
        file.write(encrypted)
    
def decrypt():
    with open('encrypted.txt', 'rb') as file:
        data = file.read()
    
    fer_obj = Fernet(generate_key())
    decrypted = fer_obj.decrypt(data)

    with open('keys.txt', 'wb') as file:
        file.write(decrypted)

if __name__ == '__main__':
    main()