import requests
from bs4 import BeautifulSoup


message = requests.get("https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526")
print(message)


soup = BeautifulSoup(message.text, 'lxml')
print(soup)
temp = soup.find('span', 'temp__value temp__value_with-unit')
print(temp)
print(temp.text)

