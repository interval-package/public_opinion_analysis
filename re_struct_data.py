import pickle
import os
import numpy as np
import pandas as pd

import sqlite3 as sql


def read_list(name):
    f = open(os.path.join("pre_process", "loading_data", name + ".pkl"), "rb")
    return pickle.load(f)


def convert_data_tab() -> pd.DataFrame:
    raw_data = read_list("processed_data")
    tags = read_list("clustered_tags")
    raw_data = np.array(raw_data)
    res = pd.DataFrame()

    res["name"] = raw_data[:, 0]
    res["date"] = raw_data[:, 1]
    res["ag"] = raw_data[:, 2]
    # res["detail"] = raw_data[:, 3]
    res["tag"] = tags
    return res


def load2_db():
    tab = convert_data_tab()
    with sql.connect(os.path.join("data", "database.db")) as conn:
        tab.to_sql("res_no_detail", con=conn, index=False)
    pass


def load2_csv():
    tab = convert_data_tab()
    tab.to_csv("res_clustering.csv", index=False)


if __name__ == '__main__':
    # print(convert_data_tab())
    pass
