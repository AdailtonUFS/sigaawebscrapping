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

site = BeautifulSoup(menu_discente_request.text, "html.parser")

turmas = site.find(id="turmas-portal")
forms = turmas.find_all('form', id=lambda value: value and 'acessarTurmaVirtualj' in value)

turmas_array = []
for form in forms:
    request_payload = {}
    form_name = form.get("name")
    request_payload['form_acessarTurmaVirtual'] = form_name

    idTurma_input = form.find('input', attrs={'name': 'idTurma'})
    if idTurma_input:
        request_payload['idTurma'] = idTurma_input.get('value')

    viewstate_input = form.find('input', attrs={'name': 'javax.faces.ViewState'})
    if viewstate_input:
        request_payload['javax.faces.ViewState'] = viewstate_input.get('value')

    request_payload[form_name + ":turmaVirtual"] = form_name + ":turmaVirtual"
    turmas_array.append(request_payload)

print(len(turmas_array))

