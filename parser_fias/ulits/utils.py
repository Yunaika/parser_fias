import requests as requests
from bs4 import BeautifulSoup


def get_html(url: str):
    page = requests.get(url)
    content = page.text
    return BeautifulSoup(content, 'html.parser')


def get_object_name_and_type(text) -> list:
    object_name_and_type = []
    idx = len(text) - 1
    for letter in text[::-1]:
        if letter.isupper():
            object_name_and_type.append(text[:idx-1])
            object_name_and_type.append(text[idx:])
            break
        else:
            idx -= 1
    return object_name_and_type


def get_fias_object(a, id) -> dict:
    """
    Get info about fias object
    :param a: object reference
    :param id: counter
    :return: dict with object info
    """
    object = dict()
    object_name_and_type = get_object_name_and_type(a.text)
    object['id'] = id
    object['name'] = object_name_and_type[0]
    object['type'] = object_name_and_type[1] if object_name_and_type[1] != 'Город' else 'Городской округ'
    object['fias_id'] = a["href"].replace('/', '')
    return object
