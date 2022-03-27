import os, subprocess
from os.path import exists
from os import path
from dotenv import load_dotenv
load_dotenv()

subprocess.call(["clear"])

def create_key(key_input):
    with open(".env","w") as file:
        key =f"keyAlphaVantage={key_input}"
        file.write(key)

def key_exist():
    return exists (".env") and path.getsize(".env") != 0

def load_key():
    keyAlphaVantage = os.getenv("keyAlphaVantage")
    return keyAlphaVantage

def remove_key_file():
    if key_exist():
        os.remove(".env")

def get_key():
    while key_exist():
        user_input = input("Do you want to work with the last session API key? (yes / no): ")
        if len(user_input) == 0:
            user_input = "invalid"
        if user_input[0].lower() == "y":
            subprocess.call(["clear"])
            break
        elif user_input[0].lower() == "n":
            remove_key_file()
            continue
        else:
            subprocess.call(["clear"])
            print("Enter a valid response or press control + c to close.")
    else:
        key_input = input("Please introduce your Alpha Vantage API key (if you don't have a key please create one for free at https://www.alphavantage.co/support/#api-key): ")
        create_key(key_input)
    
    keyAlphaVantage = load_key()
    return keyAlphaVantage

if __name__ == "__main__":
    key = get_key()
    print(key)