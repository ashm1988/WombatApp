import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://sportfix.net/app/competition.aspx?sportFixId=73d44dd0-e1a8-48ca-aaa2-990ba84ea886&sp=613&div=2741&sea=495'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

tbl = soup.findAll('table')
print(tbl[0])

for t in tbl:
    print(t)

pass
