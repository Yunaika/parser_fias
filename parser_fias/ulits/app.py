from pprint import pprint

from parser_fias.ulits.parser import parse_districts, parse_settlements
from parser_fias.ulits.work_with_csv import write_to_csv, create_csv_file_name


def save_to_csv(object: dict, name: str) -> None:
    file_name = create_csv_file_name(name)
    write_to_csv(file_name, object)


def parse_fias_subject_and_save_it_to_csv(fias_id: str) -> None:
    districts = parse_districts(fias_id)
    settlements = parse_settlements(districts)
    save_to_csv(districts, 'districts')
    save_to_csv(settlements, 'settlements')
    # pprint(settlements)
