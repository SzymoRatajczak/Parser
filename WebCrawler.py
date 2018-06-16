from bs4 import BeautifulSoup
from urllib import request
import requests
import random

def WebImage(url):
     number=random.randrange(1,10)
     name=str(number)+".png"
     request.urlretrieve(url,name)


def WebText(url):
     response=request.urlopen(url).read()
     text=str(response)
     plain=text.split("=")
     fw=fopen("plik.txt","w")
     for line in plain:
          fw.write(line)
     fw.close()


def WebCrawler(max_page,url):
     page=1
     while page < max_page:
          response=requests.get(url)
          text=response.text
          soup=BeautifulSoup(text)
          for line in soup.find_all('a',{'class':'vip'}):
               href=line.get('href')
               SelectedImage(href)
               page+=1

def SelectedImage(url):
     responose=requests.get(url)
     text=responose.text
     soup=BeautifulSoup(text)
     for line in soup.find_all('h1',{'class':'secHd'}):
          print(line.string)


WebImage("https://www.google.pl/imgres?imgurl=http://www.drapiezniki.pl/Photos/dziobak-australijski.jpg&imgrefurl=http://www.drapiezniki.pl/1332-dziobak-australijski.html&h=550&w=550&tbnid=UNo6lxR4ExNsJM:&q=dziobak&tbnh=186&tbnw=186&usg=__OALzqnXvXJpUT_GBjyEkUO5jw5U%3D&vet=10ahUKEwiK-qCbzdjbAhVGhaYKHWAsDm4Q_B0I4AEwEw..i&docid=6zzhJxaWSDNVvM&itg=1&sa=X&ved=0ahUKEwiK-qCbzdjbAhVGhaYKHWAsDm4Q_B0I4AEwEw")
WebText("https://www.ebay.pl/itm/Pirates-of-the-Caribbean-5-movie-Collection-Box-Set-Blu-ray/292236442723?hash=item440aa63c63:g:ywgAAOSwlc5Zqbj5")
WebCrawler(3,"https://www.ebay.pl/sch/Filmy-i-DVD-/11232/i.html?_catref=1")