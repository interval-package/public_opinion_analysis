import traceback

with open("baiducoo.txt") as f:
    coo = f.readline()

import requests
import json
from datetime import date, timedelta
import pandas as pd


class DownloadBaiDuIndex(object):
    def __init__(self, cookie):
        self.cookie = cookie
        self.headers = {
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://index.baidu.com/v2/main/index.html",
            "Accept-Language": "zh-CN,zh;q=0.9",
            'Cookie': self.cookie,
            "Host": "index.baidu.com",
            "X-Requested-With": "XMLHttpRequest",
            "Cipher-Text": "1656572408684_1656582701256_Nvm1pABkNsfD7V9VhZSzzFiFKylr3l5NR3YDrmHmH9yfFicm+Z9kmmwKVqVV6unvzAEh5hgXmgelP+OyOeaK8F21LyRVX1BDjxm+ezsglwoe1yfp6lEpuvu5Iggg1dz3PLF8e2II0e80ocXeU0jQFBhSbnB2wjhKl57JggTej12CzuL+h9eeVWdaMO4DSBWU2XX6PfbN8pv9+cdfFhVRHCzb0BJBU3iccoFczwNQUvzLn0nZsu0YPtG5DxDkGlRlZrCfKMtqKAe1tXQhg3+Oww4N3CQUM+6A/tKZA7jfRE6CGTFetC7QQyKlD7nxabkQ5CReAhFYAFAVYJ+sEqmY5pke8s3+RZ6jR7ASOih6Afl35EArbJzzLpnNPgrPCHoJiDUlECJveul7P5vvXl/O/Q==",

        }

    def decrypt(self, ptbk, index_data):
        n = len(ptbk) // 2
        a = dict(zip(ptbk[:n], ptbk[n:]))
        return "".join([a[s] for s in index_data])

    def get_index_data_json(self, keys, start=None, end=None):
        words = [[{"name": key, "wordType": 1}] for key in keys]
        words = str(words).replace(" ", "").replace("'", "\"")

        url = f'http://index.baidu.com/api/SearchApi/index?area=0&word={words}&area=0&startDate={start}&endDate={end}'
        print(words, start, end)
        res = requests.get(url, headers=self.headers)
        data = res.json()['data']
        uniqid = data['uniqid']
        url = f'http://index.baidu.com/Interface/ptbk?uniqid={uniqid}'
        res = requests.get(url, headers=self.headers)
        ptbk = res.json()['data']
        result = {}
        result["startDate"] = start
        result["endDate"] = end
        for userIndexe in data['userIndexes']:
            name = userIndexe['word'][0]['name']
            tmp = {}
            index_all = userIndexe['all']['data']
            index_all_data = [e for e in self.decrypt(ptbk, index_all).split(",")]
            tmp["all"] = index_all_data
            index_pc = userIndexe['pc']['data']
            index_pc_data = [e for e in self.decrypt(ptbk, index_pc).split(",")]
            tmp["pc"] = index_pc_data
            index_wise = userIndexe['wise']['data']
            index_wise_data = [e
                               for e in self.decrypt(ptbk, index_wise).split(",")]
            tmp["wise"] = index_wise_data
            result[name] = tmp
        return result

    def GetIndex(self, keys, start=None, end=None):
        today = date.today()
        if start is None:
            start = str(today - timedelta(days=8))
        if end is None:
            end = str(today - timedelta(days=2))

        try:
            raw_data = self.get_index_data_json(keys=keys, start=start, end=end)
            raw_data = pd.DataFrame(raw_data[keys[0]])
            raw_data.index = pd.date_range(start=start, end=end)

        except Exception as e:
            print(e)
            traceback.print_exc()
            raw_data = pd.DataFrame({'all': [], 'pc': [], 'wise': []})

        finally:
            return raw_data


if __name__ == '__main__':
    cookie = coo

    # 初始化一个类
    downloadbaiduindex = DownloadBaiDuIndex(cookie=cookie)

    data = downloadbaiduindex.GetIndex(keys=['三胎'], start='2021-05-31', end='2021-12-01')

    data.to_csv('data.csv', index=True)
    data.to_sql()
    pass
else:
    # import plotly.graph_objects as go
    # import pandas as pd
    # df = data
    # fig = go.Figure([go.Scatter(x=df.index, y=df['all'], fill='tozeroy')])
    # fig.update_layout(template='plotly_white', title='python 百度指数')
    # fig.show()
    # fig.write_html('third_hot.html')
    pass
