import codecs
import csv
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer


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


if __name__ == "__main__":
    """
    计算tf-idf
    https://devdocs.io/scikit_learn/modules/generated/sklearn.feature_extraction.text.tfidfvectorizer#sklearn.feature_extraction.text.TfidfVectorizer
    安装jieba：pip install -U jieba -i https://pypi.douban.com/simple/
    安装scikit-learn：pip install -U scikit-learn -i https://pypi.douban.com/simple/
    """
    yue_news_file = 'data/yule_head_10.csv'
    # 读取新闻文件
    texts = read_yue_news(yue_news_file)
    # print('texts len：{}'.format(len(texts)))
    # print('texts head 1：{}'.format(texts[0]))
    # 分词
    # print('get_tokens:{}'.format(get_tokens(texts[0])))
    texts_tokens = [get_tokens(text) for text in texts]
    raw_documents = [' '.join(tokens) for tokens in texts_tokens]
    # 计算tfidf
    tfidf_vectorizer = TfidfVectorizer()
    term_documen_matrix = tfidf_vectorizer.fit_transform(raw_documents)
    feature_names = tfidf_vectorizer.get_feature_names()
    # print('feature_names:{}'.format(feature_names))
    documen_matrix_weight = term_documen_matrix.toarray()
    for i, documen_vector_weight in enumerate(documen_matrix_weight):
        print('Top words in document {}'.format(i + 1))
        tf_idf_scores = {}
        for j in range(len(feature_names)):
            tf_idf_scores[feature_names[j]] = documen_vector_weight[j]
        sorted_words = sorted(tf_idf_scores.items(), key=lambda x: x[1], reverse=True)
        for word, tf_idf in sorted_words[:10]:
            print('word:{}\tTF-IDF:{}'.format(word, round(tf_idf, 4)))
"""
统计结果：
Top words in document 1
word:校园       TF-IDF:0.3923
word:一起       TF-IDF:0.2943
word:同过       TF-IDF:0.2943
word:海报       TF-IDF:0.2943
word:青春       TF-IDF:0.2943
word:单人       TF-IDF:0.1962
word:奇葩       TF-IDF:0.1962
word:15 TF-IDF:0.0981
word:一一       TF-IDF:0.0981
word:一出       TF-IDF:0.0981
Top words in document 2
word:袁姗姗     TF-IDF:0.4177
word:黑粉       TF-IDF:0.4177
word:希望       TF-IDF:0.1671
word:提升       TF-IDF:0.1671
word:能量       TF-IDF:0.1671
word:路演       TF-IDF:0.1671
word:一种       TF-IDF:0.0835
word:一笑       TF-IDF:0.0835
word:一页       TF-IDF:0.0835
word:三娘       TF-IDF:0.0835
Top words in document 3
word:直播       TF-IDF:0.5376
word:平台       TF-IDF:0.2481
word:花椒       TF-IDF:0.2481
word:先生       TF-IDF:0.1654
word:史航       TF-IDF:0.1654
word:家族       TF-IDF:0.1654
word:私密       TF-IDF:0.1654
word:腾飞       TF-IDF:0.1654
word:袁史       TF-IDF:0.1654
word:野蛮       TF-IDF:0.1654
Top words in document 4
word:张卫健     TF-IDF:0.6135
word:一个       TF-IDF:0.2475
word:张茜       TF-IDF:0.2454
word:猴王       TF-IDF:0.1534
word:男神       TF-IDF:0.1534
word:自己       TF-IDF:0.1237
word:北京       TF-IDF:0.1227
word:幸福       TF-IDF:0.1227
word:求婚       TF-IDF:0.1227
word:现场       TF-IDF:0.1227
Top words in document 5
word:黄河       TF-IDF:0.2639
word:慰安妇     TF-IDF:0.2262
word:抗日       TF-IDF:0.1885
word:东方       TF-IDF:0.1508
word:中国       TF-IDF:0.1508
word:八路军     TF-IDF:0.1508
word:创作       TF-IDF:0.1508
word:展现       TF-IDF:0.1508
word:战场       TF-IDF:0.1508
word:抗战       TF-IDF:0.1508
"""
