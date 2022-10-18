import os

from parser_fias.ulits.parser import parse_object
from parser_fias.ulits.work_with_csv import write_to_csv, create_csv_file_name


def parse_districts_and_save_it_to_csv(fias_id: str) -> list:
    """
    Parse districts from subject of the Russian Federation by fias id
    and save it to csv-file
    :param fias_id: id of subject
    :return: collection of districts of the subject of the Russian Federation
    """
    districts = parse_object(f'{os.getenv("BASE_URL")}/{fias_id}', 'districts')[0]
    file_name = create_csv_file_name('districts')
    write_to_csv(file_name, districts)
    return districts


def parse_settlements_and_save_it_to_csv(districts: list) -> list:
    """
    Parse settlements from all districts in subject of the Russian Federation by fias id
    and save it to csv-file
    :param districts: collection of districts of the subject of the Russian Federation
    :return: collection of settlements of districts
    """
    settlements = []
    id = 0
    for district in districts:
        if district['type'] == 'Город':
            pass
        else:
            settlement, i = parse_object(f'{os.getenv("BASE_URL")}/{district["fias_id"]}', 'settlements', id, districts)
            settlements += settlement

    file_name = create_csv_file_name('settlements')
    write_to_csv(file_name, settlements)
    return settlements
