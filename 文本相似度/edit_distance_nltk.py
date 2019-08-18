import nltk


if __name__ == "__main__":
    """
    编辑距离
    https://python.gotrained.com/nltk-edit-distance-jaccard-distance/
    安装：pip install -U nltk -i https://pypi.douban.com/simple/
    """
    sentence1 = 'abc'
    sentence2 = 'bd'
    print(nltk.edit_distance(sentence1, sentence2))  # 2
    sentence1 = 'fxy'
    sentence2 = 'fab'
    print(nltk.edit_distance(sentence1, sentence2))  # 2
