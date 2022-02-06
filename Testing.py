from ast import While
from bs4 import BeautifulSoup
import requests
import pandas as pd

#url = 'https://automatetheboringstuff.com/'
#url = 'https://boston.craigslist.org/search/sof'
url = 'https://www.programmableweb.com/category/all/apis'



#print(response,'     ',type(response))



#print(data)



d_api = {}
n_api = 0
while True:
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    apis = soup.find_all('tr')

    apis.pop(0)
    for api in apis:
        Name = api.find('a',).text
        #print(Name)   
        Link = api.find('td',{'class':'views-field views-field-pw-version-title'}).find('a').get('href')
        Link = 'https://www.programmableweb.com' + Link
        #print(Link)
        Category = api.find('td',{'class':'views-field views-field-field-article-primary-category'}).text
    # print(Category.text)
        api_response = requests.get(Link)
        api_data = api_response.text
        api_soup = BeautifulSoup(api_data, 'html.parser')
        api_description_tag = api_soup.find('div',{'class':'api_description tabs-header_description'})
        api_description = api_description_tag.text if api_description_tag else "N/A"

        n_api+=1
        d_api[n_api] = [Name, Link, Category, api_description]

    url_tag = soup.find('a',{'title':'Go to next page'})
    if url_tag.get('href'):
        url= 'https://www.programmableweb.com' + url_tag.get('href')
    else:
        break

print('Total APIs: ',n_api)
api_df = pd.DataFrame.from_dict(d_api, orient='index', columns=['api Name','api (absolute) URL','api Category','api Description'])

api_df.to_csv('apis.csv')