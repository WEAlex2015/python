import requests
from bs4 import BeautifulSoup
import csv
import os

baseUrl = 'http://www.chuangzaoshi.com'
res = requests.get(baseUrl)
soup = BeautifulSoup(res.text, "html.parser")
a = soup.select('.sidenav .nav-item a')


if(os.path.exists('test.csv')):
    os.remove('test.csv')
    with open('test.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        datas = ['cnname',	'enname', 'typetags', 'typename', 'title', 'desc',	'imgurl', 'url']
        writer.writerow(datas)

def gethtml(url, tags):
    response = requests.get(url)
    newsoup = BeautifulSoup(response.text, "html.parser")
    cnname = newsoup.select('.selected-nav-cn')[0].getText()
    enname = newsoup.select('.selected-nav-en')[0].getText()

    panels = newsoup.select('.main > .panel')
    for index in range(len(panels)):
        typename = panels[index].select('.panel-title.card')[0].getText().strip()
        items = panels[index].select('.panel-body > .row > div')
        for item in items:
            thisurl = item.select('a')[0].get('title')
            desc = item.select('a')[0].nextSibling.nextSibling.getText().strip()
            imgurl = item.select('img')[0].get('src')
            divs = item.select('a')[0].children
            for item in divs:
                if (str(item).__contains__('-title')):
                    itemsoup = BeautifulSoup(str(item), "html.parser")
                    title = itemsoup.getText().strip()
            line = []
            line.insert(0, cnname)
            line.insert(1, enname)
            line.insert(2, tags)
            line.insert(3, typename)
            line.insert(4, title)
            line.insert(5, desc)
            line.insert(6, imgurl)
            line.insert(7, thisurl)
            with open('test.csv', 'a+', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(line)

    try:
        tools = newsoup.select('.select-bar ul li a')[1].get('href')
        gethtmltools(baseUrl+tools, 'tools')
    except IndexError as e:
        print(url)

def gethtmltools(url, tags):
    response = requests.get(url)
    newsoup = BeautifulSoup(response.text, "html.parser")
    cnname = newsoup.select('.selected-nav-cn')[0].getText()
    enname = newsoup.select('.selected-nav-en')[0].getText()

    panels = newsoup.select('.main > .panel')
    for index in range(len(panels)):
        typename = panels[index].select('.panel-title.card')[0].getText().strip()
        items = panels[index].select('.panel-body > .row > div')
        for item in items:
            thisurl = item.select('a')[0].get('title')
            desc = item.select('a')[0].nextSibling.nextSibling.getText().strip()
            imgurl = item.select('img')[0].get('src')
            divs = item.select('a')[0].children
            for item in divs:
                if (str(item).__contains__('-title')):
                    itemsoup = BeautifulSoup(str(item), "html.parser")
                    title = itemsoup.getText().strip()
            line = []
            line.insert(0, cnname.strip())
            line.insert(1, enname.strip())
            line.insert(2, tags.strip())
            line.insert(3, typename.strip())
            line.insert(4, title.strip())
            line.insert(5, desc.strip())
            line.insert(6, imgurl.strip())
            line.insert(7, thisurl.strip())
            with open('test.csv', 'a+', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(line)
for item in a:
    url = item.get('href')
    gethtml(baseUrl+url, 'tags')


