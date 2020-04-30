import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def getPrice():
    url = ('https://finance.yahoo.com/quote/GC=F?p=GC=F')
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    soup = soup.find('div', class_ = "My(6px) Pos(r) smartphone_Mt(6px)")
    soup = soup.find('span', class_ = "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)").text
    print(soup)

df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/GC=F?period1=1554703806&period2=1586326206&interval=1d&events=history')
print(df.head())

