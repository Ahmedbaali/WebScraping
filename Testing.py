from bs4 import BeautifulSoup
import requests

#url = 'https://automatetheboringstuff.com/'
url = 'https://boston.craigslist.org/search/sof'

response = requests.get(url)

#print(response,'     ',type(response))

data = response.text

#print(data)

soup = BeautifulSoup(data, 'html.parser')

tags = soup.find_all('h1')

for tag in tags:
    print(tag.text)

jobs = soup.find_all('div',{'class':'result-info'})

for job in jobs:
    title = job.find('a',{'class':'result-title'}).text
    location_tag = job.find('span',{'class':'result-hood'})
    location = location_tag.text[2:-1] if location_tag else "N/A"
    date_tag = job.find('time',{'class':'result-date'})
    date = date_tag.text if date_tag else "None"
    link_tag = job.find('a',{'class':'result-title'})
    link = link_tag.get('href') if link_tag else "None"

    print('job title: ', title, '\nlocation: ', location, '\ndate: ', date, '\nlink: ', link, '\n----')