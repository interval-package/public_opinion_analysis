import jieba
import re
import logging

# 初始化结巴库


feature_list = ["赞同了该回答", ]


class str_cleaner:
    @staticmethod
    def to_raw_string(str1, has_num=False):
        """
        :cvar str1: 目标串

        将传入的目标串转化为只有数字和汉字的结果串
        """
        if has_num:
            res = re.sub('([^\u4e00-\u9fa5\u0030-\u0039])', '', str1)
        else:
            res = re.sub('([^\u4e00-\u9fa5])', '', str1)
        return res

    @staticmethod
    def cut_useless_info(tar: str, key_word=feature_list[0]):
        if '邀请回答' in tar:
            return None
        pos = tar.find(key_word)
        res = tar[pos + len(key_word):]
        res.replace('编辑于赞同条评论分享收藏喜欢收起','')
        return res

    @staticmethod
    def split_string(tar: str):
        """
        :cvar tar 目标串

        使用结巴分词将目标串进行切割，返回一个列表
        """

        seg_list = jieba.cut(tar)

        return seg_list
