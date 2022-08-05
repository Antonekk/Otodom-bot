from bs4 import BeautifulSoup
import requests
import time
from twilio.rest import Client

sid="" #add your Account SID here
authToken="" #add your Auth Token here
client=Client(sid,authToken)


newest = ""
with open("previous.txt", encoding='utf8') as file:
    newest = file.read().strip()

while True:
    #this is just an example search, you can change it like you want
    html = requests.get('https://www.otodom.pl/pl/oferty/wynajem/mieszkanie/wroclaw').text
    soup = BeautifulSoup(html, 'lxml')
    listings = soup.find_all('ul', class_='css-14cy79a e3x1uf06')
    listings = listings[1].find_all('li', class_='css-p74l73 es62z2j19')

    name = listings[0].div.h3.text
    if name!=newest:
        url = "https://www.otodom.pl" + listings[0].a['href']
        newest = name
        message = client.messages.create(
            to="whatsapp: +xxxxxxxxxxx", #add your number
            from_="whatsapp:+xxxxxxxxxxx", #add twilio number
            body=f"Nazwa: {name} \n" #example body template
                 f"Url: {url}")

        with open('previous.txt', "w" , encoding='utf8') as file:
            file.write(newest)
    print("Czekam minutę")
    time.sleep(60)