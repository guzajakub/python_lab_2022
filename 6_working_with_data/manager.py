import pandas as pd
from csv import writer
import sys


class CsvManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(f"{self.file_path}")
        pd.set_option('max_columns', 20)
        pd.set_option('max_rows', 20)

    def show_data(self):
        print(self.data)

    def append_new_data(self):
        _list = input('Type new record, separated by spaces "LastName FirstName ID Final Grade": ').split(" ")
        with open(self.file_path, 'a+', newline='') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(_list)

    def delete_row(self):
        row = int(input('Which row to delete? '))
        self.data.drop(row, axis=0, inplace=True)

    def main_menu(self):
        options = {
            1: self.show_data,
            2: self.append_new_data,
            3: self.delete_row,
            4: sys.exit
        }

        while True:
            select = int(
                input("Welcome to CSV file manager\n"
                      "1 - Show data\n"
                      "2 - Add new record\n"
                      "3 - Delete record\n"
                      "4 - Exit\n"))
            try:
                options[select]()
            except KeyError:
                print("Wrong option")


if __name__ == '__main__':
    grades = CsvManager("grades.csv")
    grades.main_menu()
