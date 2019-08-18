import numpy as np
from sklearn.metrics.pairwise import cosine_distances


if __name__ == "__main__":
    """
    cosine距离
    https://devdocs.io/scikit_learn/modules/generated/sklearn.metrics.pairwise.cosine_distances
    https://devdocs.io/scikit_learn/modules/generated/sklearn.metrics.pairwise.cosine_similarity
    安装：pip install -U scikit-learn -i https://pypi.douban.com/simple/
    """
    vector1 = np.array([1, 2, 3]).reshape(1, -1)
    vector2 = np.array([4, 7, 5]).reshape(1, -1)
    print(cosine_distances(vector1, vector2))  # [[0.07033032]]
