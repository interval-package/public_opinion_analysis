# -*- coding: utf-8 -*-
import sys
import logging
import os
import gensim
# 引入doc2vec
from gensim.models import Doc2Vec

from loading_data import get_dataset_file

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# 引入日志配置
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def train_doc2vec():
    # 加载数据
    documents = []
    # 使用count当做每个句子的“标签”，标签和每个句子是一一对应的
    count = 0

    data = get_dataset_file()

    for line in data:
        documents.append(gensim.models.doc2vec.TaggedDocument(line, [str(count)]))
        count += 1
        if count % 10000 == 0:
            logging.info('{} has loaded...'.format(count))

    # 模型训练
    model = Doc2Vec(documents, dm=1, window=8, min_count=5, workers=4)
    # 保存模型
    model.save('models/ko_d2v.model')


try:
    model = Doc2Vec.load('models/ko_d2v.model')
except Exception as e:
    logging.info("not find "+repr(e))


def get_doc_vec(tar):
    return model.infer_vector(tar)


def test_doc2vec():
    # 与标签‘0’最相似的
    print(model.docvecs.most_similar('0'))
    # 进行相关性比较
    print(model.docvecs.similarity('0', '1'))
    # 输出标签为‘10’句子的向量
    print(model.docvecs['10'])
    # 也可以推断一个句向量(未出现在语料中)
    words = u""
    print(model.infer_vector(words.split()))
