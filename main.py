from bs4 import BeautifulSoup
import requests
import time

newest = ""
with open("previous.txt", encoding='utf8') as file:
    newest = file.read().strip()

while True:
    html = requests.get('https://www.otodom.pl/pl/oferty/wynajem/mieszkanie/wroclaw?distanceRadius=0&page=1&limit=36&market=ALL&roomsNumber=%5BTHREE%5D&priceMin=1800&priceMax=3200&locations=%5Bcities_6-39%5D&viewType=listing').text
    soup = BeautifulSoup(html, 'lxml')
    listings = soup.find_all('ul', class_='css-14cy79a e3x1uf06')
    listings = listings[1].find_all('li', class_='css-p74l73 es62z2j19')
    first = True
    live_new = newest
    for i in listings:
        name = i.div.h3.text
        if name == newest:
            break
        if first:
            live_new = name
            first = False
        print(name)
        print('https://www.otodom.pl'+i.a['href'])
    newest = live_new
    with open('previous.txt', "w" , encoding='utf8') as file:
        file.write(newest)
    print("Czekam minutę")
    time.sleep(10)