import requests
import pandas as pd
import django
import sys 
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import linear_kernel


url = "https://www.mazeejpl.com/wp-json/wc/v3/products"

client_key = "ck_daa076446955d0e0e0ae43f001e5ebc48b23f5a7"
client_secret = "cs_046adb521e32db0257fb698fde9c408b2096d90a"
username = "ck_daa076446955d0e0e0ae43f001e5ebc48b23f5a7"
password = "cs_046adb521e32db0257fb698fde9c408b2096d90a"

response = requests.get(url, auth=(username, password), headers={"client_key": client_key, "client_secret": client_secret})
names=[]
if response.status_code == 200:
    # Success
    products = response.json()
    
    
    for item in products:
        names.append(item['name'])


else:
    # Handle error
    print("Error:", response.status_code)

def get_products():
    return names   
