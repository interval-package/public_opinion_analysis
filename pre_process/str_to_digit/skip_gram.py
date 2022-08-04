from gensim.models import Word2Vec


def model_train(dataset, save_model_file='template_model.model'):  # model_file_name为训练语料的路径,save_model为保存模型名
    import gensim
    import logging
    # 模型训练，生成词向量
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = gensim.models.Word2Vec(dataset)  # 训练skip-gram模型; 默认window=5
    model.save(save_model_file)
    model.wv.save_word2vec_format(save_model_file + ".bin", binary=True)
    # 以二进制类型保存模型以便重用


def get_word_vec():
    model = Word2Vec.load("third_child.model")
    tar = model.wv
    return tar


if __name__ == '__main__':
    obj = get_word_vec()
    print(obj[["三胎", "不好"]])
    pass
