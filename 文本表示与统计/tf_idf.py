import codecs
import csv
import jieba
import math

from collections import Counter


def read_yue_news(file_name):
    """读取娱乐新闻数据"""
    with codecs.open(file_name, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        texts = list()
        for row in reader:
            content = str(row['content']).strip()
            if len(content) > 0:
                texts.append(content)
        return texts


def get_tokens(text):
    """获取文本分词列表"""
    return list(jieba.cut(text))


def get_text_counter(text):
    """单词计数"""
    tokens = get_tokens(text)
    counter = Counter(tokens)
    return counter


def calculate_tf(word, text_counter, counter_sum_values):
    """计算TF"""
    return text_counter[word] / counter_sum_values


def count_word_containing(word, text_counters):
    """单词出现在各个文档中的计数"""
    return sum([1 for text_counter in text_counters if word in text_counter])


def calculate_idf(word, text_counters):
    """计算IDF"""
    return math.log(len(text_counters) / (1 + count_word_containing(word, text_counters)))


def calculate_tfidf(word, text_counter, text_counters, counter_sum_values):
    word_tf = calculate_tf(word, text_counter, counter_sum_values)
    word_idf = calculate_idf(word, text_counters)
    return word_tf * word_idf


if __name__ == "__main__":
    """
    计算tf-idf
    安装jieba：pip install -U jieba -i https://pypi.douban.com/simple/
    """
    yue_news_file = 'data/yule_head_10.csv'
    # 读取新闻文件
    texts = read_yue_news(yue_news_file)
    # print('texts len：{}'.format(len(texts)))
    # print('texts head 1：{}'.format(texts[0]))
    # 分词
    # print('get_tokens:{}'.format(get_tokens(texts[0])))
    # 单词计数
    # print('get_text_counter:{}'.format(get_text_counter(texts[0])))
    # 分词、计数
    counters = [get_text_counter(text) for text in texts]
    # 单篇文本内词汇个数统计
    counters_sum_values = [sum(counter.values()) for counter in counters]
    # print('counters_sum_values:{}'.format(counters_sum_values))
    for i, counter in enumerate(counters):
        print('Top words in document {}'.format(i + 1))
        tf_idf_scores = {word: calculate_tfidf(word, counter, counters, counters_sum_values[i]) for word in counter}
        sorted_words = sorted(tf_idf_scores.items(), key=lambda x: x[1], reverse=True)
        for word, tf_idf in sorted_words[:10]:
            print('word:{}\tTF-IDF:{}'.format(word, round(tf_idf, 4)))
    """
    统计结果:
Top words in document 1
word:校园       TF-IDF:0.0791
word:一起       TF-IDF:0.0593
word:同过       TF-IDF:0.0593
word:窗 TF-IDF:0.0593
word:海报       TF-IDF:0.0593
word:青春       TF-IDF:0.0593
word:、 TF-IDF:0.0572
word:单人       TF-IDF:0.0395
word:奇葩       TF-IDF:0.0395
word:档 TF-IDF:0.0395
Top words in document 2
word:,  TF-IDF:0.0968
word:袁姗姗     TF-IDF:0.0601
word:黑粉       TF-IDF:0.0601
word:的 TF-IDF:0.0599
word:我 TF-IDF:0.0353
word:她 TF-IDF:0.0265
word:能量       TF-IDF:0.0241
word:提升       TF-IDF:0.0241
word:路演       TF-IDF:0.0241
word:希望       TF-IDF:0.0241
Top words in document 3
word:直播       TF-IDF:0.0829
word:,  TF-IDF:0.0587
word:的 TF-IDF:0.0416
word:平台       TF-IDF:0.0383
word:花椒       TF-IDF:0.0383
word:“ TF-IDF:0.0269
word:野蛮       TF-IDF:0.0255
word:先生       TF-IDF:0.0255
word:腾飞       TF-IDF:0.0255
word:史航       TF-IDF:0.0255
Top words in document 4
word:,  TF-IDF:0.0763
word:张卫健     TF-IDF:0.0675
word:的 TF-IDF:0.0673
word:张茜       TF-IDF:0.027
word:一个       TF-IDF:0.0248
word:了 TF-IDF:0.0206
word:在 TF-IDF:0.0194
word:是 TF-IDF:0.0174
word:男神       TF-IDF:0.0169
word:猴王       TF-IDF:0.0169
Top words in document 5
word:的 TF-IDF:0.0766
word:,  TF-IDF:0.0622
word:黄河       TF-IDF:0.0291
word:慰安妇     TF-IDF:0.025
word:以 TF-IDF:0.0208
word:抗日       TF-IDF:0.0208
word:。 TF-IDF:0.0207
word:了 TF-IDF:0.0176
word:、 TF-IDF:0.0169
word:东方       TF-IDF:0.0166
    """
