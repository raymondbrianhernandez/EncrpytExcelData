"""
    Encryptor for Excel files
    Raymond Hernandez
    December 7, 2020

"""
import pandas as pd
from itsdangerous import URLSafeSerializer

MASTER_KEY = "MASTER_KEY"


def encrypt(file):
    s = URLSafeSerializer(MASTER_KEY)
    return s.dumps(file)

def open_file(excel_file):
    return pd.read_excel(excel_file)

def decrypt(json_file):
    s = URLSafeSerializer(MASTER_KEY)
    return s.loads(json_file)

def excel_to_encryption():
    excel = "data.xlsx"
    df_file = open_file(excel) # it's now DF
    df_file = df_file.to_json() # now it's JSON

    encrypted_data = encrypt(df_file) # now it's encrypted string
    file = open("data.txt", "w")
    file.write(encrypted_data)
    file.close()

def encryption_to_dataframe():
    file = open("data.txt", "r")
    encrypted_data = file.read()
    encrypted_data = decrypt(encrypted_data)
    encrypted_data = pd.read_json(encrypted_data)
    file.close()
    encrypted_data.to_excel("data.xlsx", index=False)


def main():
    excel_to_encryption()
    encryption_to_dataframe()


if __name__ == '__main__':
    main()
