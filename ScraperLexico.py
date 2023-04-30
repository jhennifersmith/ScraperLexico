import requests
from bs4 import BeautifulSoup
response = requests.get ('https://www.lexico.pt/amar/')

content = response.content
site = BeautifulSoup(content, 'html.parser')

wraps = site.find_all('div', attrs={'class' : 'card card-pl'})
card_sinonimos = wraps[0]
card_antonimos = wraps[1]
find_sinonimos = card_sinonimos.find_all('a')
find_antonimos = card_antonimos.find_all('a')

sinonimos=[]
for sinonimo in find_sinonimos:
    get = sinonimo.getText()
    sinonimos.append(get)

if len(sinonimos) == 0:
    print("Não possui sinonimos")
else:
    print(sinonimos)

antonimos=[]
for antonimo in find_antonimos:
    get = antonimo.getText()
    antonimos.append(get)

if len(antonimos) == 0:
    print("Não possui antonimos")
else:
    print(antonimos)


