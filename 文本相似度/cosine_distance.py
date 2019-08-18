import numpy as np


def calculate_cosine_distance(vector1, vector2):
    """计算cosine距离"""
    cosine_similarity = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    return 1 - cosine_similarity


if __name__ == "__main__":
    """cosine距离"""
    vector1 = np.array([1, 2, 3])
    vector2 = np.array([4, 7, 5])
    print(calculate_cosine_distance(vector1, vector2))  # 0.0703303197986318
