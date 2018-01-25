import requests

assert requests.get("https://council-tag.herokuapp.com/api/agendas/").ok is True
