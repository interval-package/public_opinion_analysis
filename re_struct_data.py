import pickle
import os
import numpy as np
import pandas as pd


def read_list(name):
    f = open(os.path.join("pre_process", "loading_data", name + ".pkl"), "rb")
    return pickle.load(f)


def convert_data_tab():
    raw_data = read_list("processed_data")
    tags = read_list("clustered_tags")
    print(tags)
    raw_data = np.array(raw_data)
    res = pd.DataFrame()

    res["name"] = raw_data[:, 0]
    res["date"] = raw_data[:, 1]
    res["ag"] = raw_data[:, 2]
    res["detail"] = raw_data[:, 3]
    res["tag"] = tags
    return res


if __name__ == '__main__':
    # print(convert_data_tab())

    tab = convert_data_tab()
    pass
