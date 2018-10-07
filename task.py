import csv


def read_csv_file(file):

    file_records = []
    reader = csv.DictReader(open(file))

    for row in reader:
        file_records.append(dict(row))

    return file_records


print(read_csv_file("CSV.csv"))
