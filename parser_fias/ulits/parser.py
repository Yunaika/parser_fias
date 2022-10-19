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
