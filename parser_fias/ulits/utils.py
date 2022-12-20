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
    object['type'] = reduce_type(object_name_and_type[1] if object_name_and_type[1] != 'Город' else 'Городской округ')
    object['fias_id'] = a["href"].replace('/', '')
    return object


def reduce_type(type: str) -> str:
    replace_dict = {'Городской округ': 'г.о.', 'Городское поселение': 'г.п.', 'Сельское поселение': 'с.п.',
                    'Внутригородской район': 'вн.р-н', 'Поселение': 'пос.', 'Район': 'р-н', 'Сельсовет': 'с/с',
                    'Город': 'г.', 'Поселок городского типа':' пгт.', 'Рабочий поселок': 'рп.',
                    'Курортный поселок': 'кп.', 'Городской поселок': 'гп.', 'Поселок': 'п.', 'Выселки(ок)': 'в-ки',
                    'Городок': 'г-к', 'Заимка': 'з-ка', 'Починок': 'п-к', 'Кишлак': 'киш.', 'Местечко': 'м-ко',
                    'Деревня': 'д.', 'Село': 'с.', 'Слобода': 'сл.', 'Станция': 'ст.', 'Станица': 'ст-ца',
                    'Улус': 'у.', 'Хутор': 'х.', 'Разъезд': 'рзд.', 'Зимовье': 'зим.', 'Кордон': 'кор.',
                    'Населенный пункт': 'н.п.'}
    for key, value in replace_dict.items():
        if type == key:
            type = value
            break

    return type
