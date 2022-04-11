import os
from datetime import datetime
from pandas import read_csv


class ExtractTransformLoad:

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = read_csv(self.csv_file)
        self.number_of_rows, self.number_of_columns = self.data.shape
        self.file_size  = float(os.stat(csv_file).st_size / 1024)
        self.content = self.data.to_dict('records')
        self.columns_name = self.data.columns[0]
