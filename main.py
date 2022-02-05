from bs4 import BeautifulSoup
import requests

url = 'https://automatetheboringstuff.com/'

response = requests.get(url)

#print(response,'     ',type(response))

data = response.text

#print(data)

soup = BeautifulSoup(data, 'html.parser')

tags = soup.find_all('h1')

for tag in tags:
    print(tag.text)