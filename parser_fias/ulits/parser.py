from parser_fias.ulits.utils import get_html, get_fias_object


def parser_object(url: str, type: str, i=0, districts=None) -> dict:
    """
    Сollection of information about the object
    :param url: object url
    :param type: object type
    :param i: counter
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
            fias_object = get_fias_object(a, i)
            if type == 'settlements':
                # добавить дистрикт id
                district_name = html.find('h1').text.rsplit(',', 1)[0]
                for district in districts:
                    if district['name'] == district_name:
                        fias_object['district_id'] = district['id']
            udm_objects.append(fias_object)
            i += 1
    return udm_objects, i
