import pymysql
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv
import os
import time

#res = requests.get("https://finance.yahoo.com/commodities", verify = False)
res = requests.get("https://finance.yahoo.com/commodities")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))[0]

n = len(df)
i = 0
miConexion = pymysql.connect( host='localhost', user= 'root', passwd='', db='mercados' )

for i in range(i,n):
    reg = df.to_csv(index=False, sep =';')
    indice = df.loc[i, 'Symbol']
    symbol = df.loc[i, 'Symbol']
    nme = df.loc[i, 'Name']
    lastprice =  str(df.loc[i, 'Last Price'])
    #lastprice = lastprice.replace(",", ".")
    mktime = df.loc[i, "Market Time"]
    chnge = str(df.loc[i, "Change"])
    pchange = str(df.loc[i, "% Change"])
    pchange = pchange.replace("%", "")
    volume =  str(df.loc[i, "Volume"])
    opnint = str(df.loc[i, "Open Interest"])
    fcarga = time.strftime("%Y/%m/%d")
    hcarga = time.strftime("%H:%M:%S")

    cur = miConexion.cursor()
    cur.execute ( "INSERT INTO cmdtis (symbol, nme, lastprice, mktime, chnge, pchange, volume, opnint, fcarga, hcarga) VALUES ('" + symbol + "', '" + nme + "', " + lastprice + ", '" + mktime + "', " + chnge + ", " + pchange + ", " + volume + ", " + opnint + ", '" + fcarga + "', '" + hcarga + "')")
    miConexion.commit()
    #print(i)
    i = i + 1 
        
miConexion.close()




