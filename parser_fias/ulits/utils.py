import requests as requests
from bs4 import BeautifulSoup


def get_html(url: str):
    page = requests.get(url)
    content = page.text
    BeautifulSoup(content, 'html.parser')
    return BeautifulSoup(content, 'html.parser')


def get_fias_object(a, i):
    """
    Get info about fias object
    :param a: object reference
    :param i: counter
    :return: object info
    """
    object = dict()
    object['id'] = i
    object['name'] = a.text
    object['type'] = a.text.rsplit(' ', 1)[1]
    object['fias_id'] = a["href"].replace('/', '')
    return object


