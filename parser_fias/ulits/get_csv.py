import os

from parser_fias.ulits.parser import parser_object
from parser_fias.ulits.work_with_csv import write_in_csv


def get_csv_with_districts(url):
    file_name = r'..\csv\districts.csv'
    districts = parser_object(f'{os.getenv("BASE_URL")}/{url}', 'districts')[0]
    write_in_csv(file_name, districts)
    return districts


def get_csv_with_settlements(districts):
    file_name = f'../csv/settlements.csv'

    settlements = []
    i = 0
    for item in districts:
        if item['type'] == 'Город':
            pass
        else:
            settlement, i = parser_object(f'{os.getenv("BASE_URL")}/{item["fias_id"]}', 'settlements', i, districts)
            settlements += settlement
    write_in_csv(file_name, settlements)
