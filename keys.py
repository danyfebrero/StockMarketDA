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
    while key_exist() == False:
        key_input = input("Please introduce your Alpha Vantage API key (if you don't have a key please create one for free at https://www.alphavantage.co/support/#api-key): ")
        if len(key_input) == 0:
            continue
        create_key(key_input)
    keyAlphaVantage = load_key()
    return keyAlphaVantage

if __name__ == "__main__":
    key = get_key()
    print(key)