import csv
import os


def create_csv_file_name(name: str) -> str:
    """
    :return: full file name
    """
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\\..')
    return f'{path}/csv/{name}.csv'


def write_to_csv(file_name, data: dict) -> None:
    """
    Create CSV file with data
    :return: None
    """
    with open(file_name, mode="w", encoding='utf-8') as w_file:
        names = data[0].keys()
        file_writer = csv.DictWriter(w_file, delimiter=",",
                                     lineterminator="\n", fieldnames=names)
        file_writer.writeheader()
        file_writer.writerows(data)
