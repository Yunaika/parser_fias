import os
from parser_fias.ulits.get_csv import get_csv_with_districts, get_csv_with_settlements


os.environ['BASE_URL'] = 'https://xn--80ap2aj.xn--80asehdb'
districts = get_csv_with_districts('52618b9c-bcbb-47e7-8957-95c63f0b17cc')
get_csv_with_settlements(districts)

