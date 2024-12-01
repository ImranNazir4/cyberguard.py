import pandas as pd
import numpy as np
import streamlit as st
import requests
import json
import sys
import colorama
from time import sleep 
import json
from dotenv import load_dotenv
# Load environment variables
load_dotenv()

st.subheader("Malicious File Scanner")


selection=st.sidebar.selectbox("Select",("Cyber Awareness Chatbot","Malicious File Scanner"))



file=st.file_uploader("Select a File")


colorama.init()
def type(words: str):
    for char in words:
        sleep(0.015)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

url = r'https://www.virustotal.com/vtapi/v2/file/scan'

# api = open("vt-api.txt", "r").read()


# file_path = colorama.Fore.YELLOW + "cui2020.pdf"
# params = {"apikey": api}

with open(file.name, mode='wb') as w:
        w.write(file.getvalue())

file_to_upload = {"file": open(file.name, "rb")}

response = requests.post(url,files = file_to_upload , params=params)
file_url = f"https://www.virustotal.com/api/v3/files/{(response.json())['sha1']}"

headers = {"accept": "application/json", "x-apikey": api}
type(colorama.Fore.YELLOW + "Analysing....")

response = requests.get(file_url,headers=headers)

report = response.text
report = json.loads(report)
# json_string = json.dumps(report)

st.write(response)
