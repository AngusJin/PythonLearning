import requests
import re
import json


base_url = 'https://www.baidu.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

response = requests.get(base_url, headers=headers)
data = response.text
print(data)
