import os
from copy import deepcopy
from dotenv import load_dotenv
from parser_fias.ulits.utils import get_html, get_fias_object


def parse_object(url: str, type: str, id=0, districts=None) -> list:
    """
    Collect of information about the object
    :param url: object url
    :param type: object type
    :param id: counter
    :param districts: main object
    :return: collection of objects and counter
    """
    html = get_html(url)
    udm_objects = []
    t = html.find_all('div', class_='row')
    for div_item in t[1].find_all('div', class_='col-12'):
        if 'Элемент планировочной структуры' in div_item.text:
            break
        for a in div_item.find_all('a'):
            fias_object = get_fias_object(a, id)
            if type == 'settlements':
                # добавить id района
                district_name = html.find('h1').text.rsplit(',', 1)[0]
                for district in districts:
                    if district['name'] in district_name:
                        fias_object['district_id'] = district['id']
            udm_objects.append(fias_object)
            id += 1
    return udm_objects, id


def parse_districts(fias_id: str) -> list:
    """
    Parse districts from subject of the Russian Federation by fias id
    :param fias_id: id of subject
    :return: collection of districts of the subject of the Russian Federation
    """
    load_dotenv()
    districts = parse_object(f'{os.getenv("BASE_URL")}/{fias_id}', 'districts')[0]

    return districts


def parse_settlements(districts: list) -> list:
    """
    Parse settlements from all districts in subject of the Russian Federation by fias id
    and save it to csv-file
    :param districts: collection of districts of the subject of the Russian Federation
    :return: collection of settlements of districts
    """
    settlements, cities = [], []
    id = 0
    for district in districts:
        if district['type'] == 'Городской округ':
            city = deepcopy(district)
            city['district_id'] = district['id']
            city['id'] = id
            city['type'] = 'Город'
            id += 1
            settlements.append(city)
        else:
            settlement, id = parse_object(f'{os.getenv("BASE_URL")}/{district["fias_id"]}', 'settlements',
                                          id, districts)
            settlements += settlement

    return settlements
