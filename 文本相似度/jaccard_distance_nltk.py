import nltk


if __name__ == "__main__":
    """
    jaccard距离
    https://python.gotrained.com/nltk-edit-distance-jaccard-distance/
    """
    words1 = ['I', 'like', 'apple']
    words2 = ['I', 'do', 'not', 'like', 'apple']
    # you must first convert them to the set type
    print(nltk.jaccard_distance(set(words1), set(words2)))  # 0.4
    words1 = '123'
    words2 = '12345'
    print(nltk.jaccard_distance(set(words1), set(words2)))  # 0.4
