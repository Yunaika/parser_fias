import os
from parser_fias.ulits.app import parse_districts_and_save_it_to_csv, parse_settlements_and_save_it_to_csv


os.environ['BASE_URL'] = 'https://xn--80ap2aj.xn--80asehdb'
districts = parse_districts_and_save_it_to_csv('52618b9c-bcbb-47e7-8957-95c63f0b17cc')
settlements = parse_settlements_and_save_it_to_csv(districts)

