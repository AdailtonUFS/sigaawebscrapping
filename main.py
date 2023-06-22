import requests
from bs4 import BeautifulSoup
from src.url_mapper import urls
from decouple import config

session = requests.Session()

# Faz o login no site
login_data = {
    'user.login': config('USER-LOGIN'),
    'user.senha': config('USER-PASSWORD')
}
loginRouter = urls['login']
session.post(loginRouter.url, data=login_data)

menuDiscenteRouter = urls['menu_discente']
menu_discente_request = session.get(menuDiscenteRouter.url)
print(menu_discente_request.text)



site = BeautifulSoup(menu_discente_request.text, "html.parser")

print(site.find(id="turmas-portal"))


