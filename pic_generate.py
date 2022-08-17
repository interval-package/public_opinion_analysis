import matplotlib.pyplot as plt

from sql_reading import *


def draw_bar_tags_hist():
    tab = calc_tags()
    res = tab.values
    print(res)
    plt.bar(res[:, 0], res[:, 1])
    plt.xlabel("our tags")
    plt.ylabel("tag counts")
    plt.show()


def draw_time_series():
    _tab = [calc_tags_time_series(0)]
    for tab in _tab:
        plt.subplot(1, 2, 1)
        plt.plot(tab["date"], tab["num"], 'b*-')
        plt.xlabel("time")
        plt.ylabel("number of comments")
        plt.legend(["l1-number of comments"])
        plt.subplot(1, 2, 2)
        plt.plot(tab["date"], tab["ags"], 'r*-')
        plt.xlabel("time")
        plt.ylabel("number of likes")
        plt.legend(["l2-number of likes"])
        plt.show()
    pass


if __name__ == '__main__':
    draw_time_series()
    pass
