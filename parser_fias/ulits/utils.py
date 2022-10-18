import requests as requests
from bs4 import BeautifulSoup


def get_html(url: str):
    page = requests.get(url)
    content = page.text
    return BeautifulSoup(content, 'html.parser')


def get_fias_object(a, id) -> dict:
    """
    Get info about fias object
    :param a: object reference
    :param id: counter
    :return: dict with object info
    """
    object = dict()
    object['id'] = id
    object['name'] = a.text
    object['type'] = a.text.rsplit(' ', 1)[1]
    object['fias_id'] = a["href"].replace('/', '')
    return object
