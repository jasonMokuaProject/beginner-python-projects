import base64
import json
import hashlib

from main import decrypted_message

username_and_passwords = []

def readPassAndUser():
    with open("passwords_Manager.txt") as r:
        for line in r:
            user_obj = json.loads(line)
            username_and_passwords.append(user_obj)

readPassAndUser()
def saveUsersandPass(pass_and_user):
    with open("passwords_Manager.txt","w") as f:
        for pu in pass_and_user:
           f.write(json.dumps(pu) +" \n")


def CreateKey():
    thekey = input("Enter your master password: ").strip()
    return hashlib.sha256(thekey.encode()).digest()


def encrypt_and_decrypt(the_data,key):
    the_data = the_data.encode()
    encrypted_message = bytes([b ^ key[i % len(key)] for i,b in enumerate(the_data)])
    return encrypted_message.hex()


def decrypt_message(the_data,key):
    the_data = bytes.fromhex(the_data)
    decrypted_message = bytes([b ^ key[i % len(key) ] for i,b in enumerate(the_data)])
    return decrypted_message.decode(errors="ignore")


def main():
    ContinueRunning = True
    key = CreateKey()
    while ContinueRunning:
        print("Password Manager ")
        print("---------------------------------")
        print(" 1) Add Username And Password ")
        print(" 2) show Usernames And Password")
        print(" 3) Exit Script")
        user_option = int(input("Enter The Number Of The Task: "))

        if user_option == 1:
            print("user option 1")
            username = str(input("Enter the username: "))
            password = str(input("Enter the password: "))
            u_and_p = {"username":encrypt_and_decrypt(username,key),"password":encrypt_and_decrypt(password,key)}
            username_and_passwords.append(u_and_p)
            saveUsersandPass(username_and_passwords)

        elif user_option == 2:
            for x in username_and_passwords:
                print(f" Username: {decrypt_message(x['username'],key)} \t Password: {decrypt_message(x['password'],key)}")

        elif user_option == 3:
            print("GoodBye !")
            ContinueRunning = False

main()
