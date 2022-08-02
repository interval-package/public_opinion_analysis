import pandas as pd
import csv

_csv_path = "../data/outside_data/jf_violence.csv"


def load_data(tar_path=_csv_path):
    tb = pd.read_csv(tar_path)
    print(tb, error_bad_lines=False)


def traverse_csv(tar_path=_csv_path, process_func=print):
    with open(tar_path, encoding='utf-8-sig') as f:
        for row in csv.reader(f, skipinitialspace=True):
            process_func(row)


if __name__ == '__main__':
    traverse_csv()
