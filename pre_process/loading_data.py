import pandas as pd
import numpy as np
import csv
from utils import str_cleaner
from os import path

_csv_path_jf = "../data/outside_data/jf_violence.csv"

_csv_path_3c = "../data/outside_data/third_child.csv"


def load_data(tar_path=_csv_path_jf):
    tb = pd.read_csv(tar_path)
    print(tb, error_bad_lines=False)


def traverse_csv(tar_path=_csv_path_jf, process_func=print):
    with open(tar_path, encoding='utf-8-sig') as f:
        for row in csv.reader(f, skipinitialspace=True):
            process_func(row)


def cleaned_str_list_get(row):
    row = row[-1]
    row = str_cleaner.to_raw_string(row) + "\n"
    row = str_cleaner.cut_useless_info(row)
    return row


def gather_info(row, res: list, has_ag=True) -> None:
    ques = cleaned_str_list_get(row)
    if ques is not None:
        if len(ques) < 6:
            pass
        else:
            temp = []
            if has_ag:
                temp.append(str_cleaner.get_agree(row[4]))
            temp.append(ques)
            res.append(temp)
    return


if __name__ == '__main__':
    buffer = []
    traverse_csv(_csv_path_3c, process_func=lambda row: gather_info(row, buffer))
    print(np.array(buffer)[:,1])
