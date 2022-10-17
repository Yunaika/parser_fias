import requests as requests
from bs4 import BeautifulSoup

from parser_fias.parser_udmurtia import base_url
from parser_fias.ulits.parser import parser_object
from parser_fias.ulits.work_with_csv import write_csv


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


def get_csv_with_districts(url):
    file_name = r'..\csv\districts.csv'
    districts = parser_object(f'{base_url}/{url}', 'districts')[0]
    write_csv(file_name, districts)
    return districts


def get_csv_with_settlements(districts):
    file_name = f'../csv/settlements.csv'

    settlements = []
    i = 0
    for item in districts:
        if item['type'] == 'Город':
            pass
        else:
            settlement, i = parser_object(f'{base_url}/{item["fias_id"]}', 'settlements', i, districts)
            settlements += settlement
    write_csv(file_name, settlements)
