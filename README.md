# 尖叫效应与信息茧房

## 数据采集

### 知乎评论

使用爬虫，从知乎上爬取相关问题回答：

| 问题       | 关键字                 |
| ---------- | ---------------------- |
| 蒋劲夫家暴 | 蒋劲夫打人，蒋劲夫家暴 |
| 三胎政策   | 三胎，三宝             |

### 百度指数

我们基于百度指数，判断某个话题的总体热度情况

## 数据处理

### 文字化

我们针对每一个回答，都将所有内容转化为一个纯汉字的字符串，然后使用“`jieba`分词”，转化为目标列表

### 得分评价

使用`tf-idf`基于全局的语料库进行评分，获得评分结果

#### 向量化

`word2vec`

word-vec的话就是将词语转化为向量。有两大类模型：

- CBOW模型(Continuous Bag-of-Words Model)与Skip-gram模型
  - sg是通过训练一个神经网络，将文字作为输入，输出一个一个目标的向量

## 聚类标签化

针对我们第一步进行的数据预处理，我们对获得的向量使用k-means模型进行聚类分析

我们将目标的类型分为一下大类

| 类型 | 描述 |
| ---- | ---- |
|      |      |
|      |      |
|      |      |

### 时间序列模型

*这里是一个分析点，使用时间序列进行传播类型的分析*

对于每一个评论，我们会有对应的时间以及聚类的标签类型，我们可以得到不同类型评论随着时间变化的分布图。

结合百度热度图，我们可以有基本的分析

## 尖叫效应评价模型

| 变量     |            |
| -------- | ---------- |
| 赞同数   | 影响力分析 |
| 文字长度 |            |
| 类型标签 |            |
|          |            |

