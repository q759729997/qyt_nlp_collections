import nltk


if __name__ == "__main__":
    """
    编辑距离
    https://python.gotrained.com/nltk-edit-distance-jaccard-distance/
    """
    words_set1 = {'I', 'like', 'apple'}
    words_set2 = {'I', 'do', 'not', 'like', 'apple'}
    print(nltk.jaccard_distance(words_set1, words_set2))  # 0.4
