import pandas as pd
import jieba
import gensim

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.cluster import KMeans


class FactorProcess:

    def __init__(self):
        from loading_data import get_dataset_file
        self.data = get_dataset_file()
        from doc2vec import get_doc_vec
        self.vec = [get_doc_vec(line) for line in self.data]

    def extract_info_Ti_Dif(self):
        # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
        vectorizer = CountVectorizer(max_features=10)
        # 该类会统计每个词语的tf-idf权值
        tf_idf_transformer = TfidfTransformer()
        # 将文本转为词频矩阵并计算tf-idf
        tf_idf = tf_idf_transformer.fit_transform(vectorizer.fit_transform(self.data))
        # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
        x_train_weight = tf_idf.toarray()

        # self.encode_weight = x_train_weight
        return x_train_weight

    def clustering(self, is_save=True):
        weight = self.vec
        clf = KMeans(n_clusters=20)
        res = clf.fit(weight)
        print("the center:")
        print(clf.cluster_centers_)
        return clf.labels_

    def clustering_save_tags(self):
        import pickle
        pickle.dump(self.clustering(), open("loading_data/clustered_tags.pkl", 'wb'))

    def normalize_vec(self):

        return


if __name__ == '__main__':
    obj = FactorProcess()
    print(obj.vec)
    obj.clustering_save_tags()
    pass
