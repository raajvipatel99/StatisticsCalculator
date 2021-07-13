import csv
from pprint import pprint
from FileUtilities.absolutepath import absolutepath


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data.clear()
        with open(absolutepath(filepath)) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass
