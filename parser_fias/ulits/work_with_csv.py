import csv


def write_csv(file_name, info: dict):
    with open(file_name, mode="w", encoding='utf-8') as w_file:
        names = info[0].keys()
        file_writer = csv.DictWriter(w_file, delimiter=",",
                                     lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        file_writer.writerows(info)
