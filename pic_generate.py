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
    tab = method_read_by_tag()

    pass


if __name__ == '__main__':
    draw_time_series()
    pass
