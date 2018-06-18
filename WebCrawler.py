import requests
from bs4 import BeautifulSoup
import operator
def WebCrawler(url):
     dirt_list=[]
     page=requests.get(url).text
     soup=BeautifulSoup(page)
     for line in soup.find_all('a',{'class':'vip'}):
          content=line.string.split()
          for i in content:
               print(i)
               dirt_list.append(i)
          clean_up_list(dirt_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        accepted = "abcdefghijklmnopqrstuvwxyz\'"
        for c in list(word):
            if c not in list(accepted):
                word = word.replace(c, "")
        if len(word) > 0:
            print(word)
            clean_word_list.append(word)
            dicto(clean_word_list)

def dicto(lista):
     dictionary={}
     for word in lista:
          if word not in dictionary:
               dictionary[word]=1
          else:
               dictionary[word]+=1
     for key,value in sorted(dictionary.items(),key=operator.itemgetter(1)):
          print(key,value)

WebCrawler("https://www.ebay.pl/sch/Filmy-i-DVD-/11232/i.html?_catref=1")