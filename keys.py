import os, subprocess
from os.path import exists
from os import path
from dotenv import load_dotenv
load_dotenv()

subprocess.call(["clear"])

def save_key():
    with open(".env","w") as file:
        key_input = input("Please introduce your Alpha Vantage API key (if you don't have a key please make one for free at https://www.alphavantage.co/support/#api-key): ")
        key =f"keyAlphaVantage={key_input}"
        file.write(key)

if exists (".env") and path.getsize(".env") != 0:
    while True:
        user_input = input("Do you want to work with the last session API key? (yes / no): ")
        if user_input[0].lower() == "y" or user_input[0].lower() == "n":
            break
        else:
            subprocess.call(["clear"])
            print("Enter a valid response or press control + c to close.")
    if user_input[0].lower() == "n":
        save_key()
else:
    save_key()

subprocess.call(["clear"])
keyAlphaVantage = os.getenv("keyAlphaVantage")