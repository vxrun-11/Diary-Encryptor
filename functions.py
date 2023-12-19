"""
Program Made by :
    Nanda Pranesh.S - 21pc19
    Varun.s         - 21pc25

Note:
    The program doesnt't work without it's main counterpart
"""



import pickle
from cryptography.fernet import Fernet
import hashlib
import uuid
import os
    
def gen_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    key_file = open("encryptkey.dat", "wb")
    pickle.dump(key,key_file)
    key_file.close()
    
def load_key():
    """
    Loads the key named `encryptkey.dat` from the current directory.
    """
    file = open("encryptkey.dat", "rb")
    try:    
        key = pickle.load(file)
    except EOFError:
        file.close()
    return key

def encrypt_and_store(data,username):
    """
    Encrypts Data and stores in File
    """
    key = load_key()
    encoded = data.encode()
    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    file = open(username+".dat","wb")
    file.write(encrypted)
    file.close()
    

def hash_gen(password):
    """
    Converts given String to Hash Value
    """
    # UUID is used to generate a random number
    salt = str(uuid.uuid4())
    return str(hashlib.sha256((salt + password).encode()).digest()) + ':' + salt

def hash_store(username,hashed):
    """
    Stores the Hashed Password into the safefile
    """
    file = open("userdata.dat","rb")
    raw = file.read().decode()
    if raw == "":
        listmain = {}
    else:
        listmain = eval(raw)
    listmain[username] = hashed
    file.close()
    os.remove("userdata.dat")
    file = open("userdata.dat","wb")
    file.write(str(listmain).encode())
    file.close()
    
def hash_check(username,userpass):
    """
    Opens the Safe file and checks user's password with available data
    """
    file = open("userdata.dat","rb")
    raw = file.read()
    if raw == b'':
        return "Account Doesn't Exist"
    else:
        listmain = eval(raw.decode())
        file.close()
     
    hashed_password = listmain[username]
    password, salt = hashed_password.split(':')
    if password == str(hashlib.sha256((salt + userpass).encode()).digest()):
        return "Login Success"
    else:
        return "Password Incorrect"

def username_check(username):
    """
    Checks whether the username already exists in file
    """
    try:
        file = open("userdata.dat","rb")
        raw = file.read()
        dictmain = eval(raw.decode())
        if username in dictmain:
            return True
        else:
            return False
        file.close()
    except:
        pass

def new_user_file(username):
    """
    Creates a new file for the user upon registering new account
    """
    file = open(username+".dat","wb")
    file.close()

def initialize():
    """
    Creates Missing Files if any
    """
    path = "userdata.dat"
    if not os.path.exists(path):
        file = open("userdata.dat","wb")
        file.close()
    if not os.path.exists("encryptkey.dat"):
        gen_key()
    