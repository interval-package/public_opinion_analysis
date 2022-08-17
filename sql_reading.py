import sqlite3 as sql
import os

import pandas as pd
import numpy as np
from datetime import datetime
import time
import matplotlib.pyplot as plt

conn = sql.connect(os.path.join("data", "database.db"))


def method_read_by_tag(tag=None, time_simplify=True) -> pd.DataFrame:
    if tag is None:
        query = "select * from res_no_detail order by date"
    else:
        query = "select * from res_no_detail where tag = {} order by date".format(str(tag))
    _tab = pd.read_sql_query(sql=query, con=conn)
    if time_simplify:
        _tab.loc[:, "date"] = _tab.loc[:, "date"].apply(lambda res: res[:7])
    return _tab


# def method_read_time_


def calc_tags(is_save=False):
    query = "select tag, count(*) from res_no_detail group by tag order by tag"
    tab = pd.read_sql_query(sql=query, con=conn)
    if is_save:
        tab.to_csv("data/tags_calc.csv", index=False)
    return tab


def calc_tags_time_series(tag=0):
    query = "select date, count(*) as num, sum(ag) as ags from dateless where tag = {} group by date".format(str(tag))
    tab = pd.read_sql_query(sql=query, con=conn)
    tab["date"] = tab["date"].apply(lambda tar: datetime.strptime(tar, "%Y-%m"))
    return tab


if __name__ == '__main__':
    tab = calc_tags_time_series()
    print(tab)
    # tab.to_sql("dateless", con=conn, index=False)
    pass
