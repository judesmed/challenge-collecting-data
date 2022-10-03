
import asyncio
import httpx
from bs4 import BeautifulSoup
import re
from requests_html import HTMLSession
import requests
url = "https://www.immoweb.be/en/classified/apartment/for-sale/deinze/9800/10130388?searchId=63341f64bc8e6"


r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")
data = {}
for l in soup.html.find_all("tr"):
    if l.find("th"):
        a = str(l.find("th"))
        a = re.sub("<([^<]*)>", "", a)
        a = a.strip()
        a = a.replace("\n", "")
        a = a.replace("\t", "")
        if a is not None:
            th = a
        
        
    if l.find("td"):
        a = str(l.find("td"))
        a = re.sub("<([^<]*)>", "", a)
        a = a.strip()
        a = a.replace("\n", "")
        a = a.replace("\t", "")
        a = re.sub("\ {2,}",' ',a)
        td = a

    data[th] = td    

print (data)





