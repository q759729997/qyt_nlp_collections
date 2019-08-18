def calculate_jaccard_distance(words1, words2):
    """计算jaccard距离"""
    # 转换为set集合
    words_set1 = set(words1)
    words_set2 = set(words2)
    # 计算交集与并集
    union_len = len(words_set1.union(words_set2))  # 两个集合的并集
    intersection_len = len(words_set1.intersection(words_set2))  # 两个集合的交集
    return 1 - intersection_len / union_len


if __name__ == "__main__":
    """
    jaccard距离
    """
    words1 = ['I', 'like', 'apple']
    words2 = ['I', 'do', 'not', 'like', 'apple']
    print(calculate_jaccard_distance(words1, words2))  # 0.4
    words1 = '123'
    words2 = '12345'
    print(calculate_jaccard_distance(set(words1), set(words2)))  # 0.4
