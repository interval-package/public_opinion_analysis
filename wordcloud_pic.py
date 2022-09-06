import wordcloud
import matplotlib.pyplot as plt
import matplotlib
import pickle
import numpy as np
import pandas as pd

# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号


def to_db():
    import sqlite3
    tab = pd.DataFrame(columns=["word", "weight"])

    tf_idf = pickle.load(open("pre_process/if_idf_for_word.pkl", "br"))
    temp = np.array([[i[0], i[1]] for i in tf_idf])

    tab["word"] = temp[:, 0]
    tab["weight"] = temp[:, 1]

    print(tab)

    tab.to_sql(name="tf_weights", con=sqlite3.connect("data/database.db"), index=False)
    pass


def from_db():
    import sqlite3
    return pd.read_sql_query(sql="select * from tf_weights", con=sqlite3.connect("data/database.db"))


tar = from_db()
print(tar)

tar.to_csv("./data/tf_weights.csv")


def generate_weight_bar(nums=10):
    plt.bar(tar.loc[:nums, "word"], tar.loc[:nums, "weight"])
    plt.show()
    pass


generate_weight_bar()


def generate_word_cloud_pic():
    wd = wordcloud.wordcloud.WordCloud()
    wd.generate_from_frequencies()
    pass
