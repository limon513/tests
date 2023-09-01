from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.parsehub.com/').text
soup = BeautifulSoup(source,'lxml')

print(soup.prettify())