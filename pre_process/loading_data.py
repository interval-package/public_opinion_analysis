import logging
import os

import pandas as pd
import numpy as np
import csv
from utils import str_cleaner
from os import path
import pickle

_csv_path_jf = "../data/outside_data/jf_violence.csv"

_csv_path_3c = "../data/outside_data/third_child.csv"


def load_data(tar_path=_csv_path_jf):
    tab = pd.read_csv(tar_path)


def traverse_csv(tar_path=_csv_path_jf, process_func=print):
    with open(tar_path, encoding='utf-8-sig') as f:
        for row in csv.reader(f, skipinitialspace=True):
            process_func(row)


def cleaned_str_list_get(row):
    row = row[-1]
    row = str_cleaner.to_raw_string(row) + "\n"
    row = str_cleaner.cut_useless_info(row)
    return row


def gather_info_raw(row, res: list) -> None:
    res.append(row)
    pass


def gather_info(row, res: list, has_other=False) -> None:
    ques = cleaned_str_list_get(row)
    if ques is not None:
        if len(ques) < 6:
            pass
        else:
            ques = str_cleaner.split_string(ques)
            if has_other:
                temp = []
                user = row[2][0]
                date = row[3][4:]
                ag = str_cleaner.get_agree(row[4])
                temp.append(user)
                temp.append(date)
                temp.append(ag)
                temp.append(ques)
                res.append(temp)
            else:
                res.append(ques)
    pass


def get_dataset(has_other=True, func=gather_info):
    buffer = []
    # generate new list
    traverse_csv(_csv_path_3c, process_func=lambda row: func(row, buffer, has_other))
    return buffer


def get_dataset_file(tar_file="cut_words.pkl") -> list:
    tar = os.path.join("loading_data", tar_file)
    if os.path.exists(tar):
        f1 = open(tar, 'rb')
        obj = pickle.load(f1)
        return obj
    else:
        raise FileNotFoundError("error space")


def save_data(tar: list, file_name="temp.pkl"):
    f1 = open(file_name, 'wb')
    pickle.dump(tar, f1)
    pass


if __name__ == '__main__':
    data = get_dataset(True)
    print(data)
    save_data(data, "loading_data/processed_data.pkl")
    pass
