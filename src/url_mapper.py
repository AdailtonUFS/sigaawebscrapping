from decouple import config
from src.Entities.Router import Router

urls: dict = {
    'login': Router("login", "POST", config('URL_SIGAA') + "logar.do?dispatch=logOn"),
    'menu_discente': Router("menu_discente", "GET", config('URL_SIGAA') + "portais/discente/discente.jsf"),
}
