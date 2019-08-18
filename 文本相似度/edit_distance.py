import numpy as np


def calculate_levenshtein_edit_distance(sentence1, sentence2):
    """计算编辑距离"""
    sentence1_len = len(sentence1)
    sentence2_len = len(sentence2)
    # 初始化矩阵
    dp = np.zeros((sentence1_len + 1, sentence2_len + 1))
    for i in range(sentence1_len + 1):
        dp[i][0] = i
    for j in range(sentence2_len + 1):
        dp[0][j] = j
    for i in range(1, sentence1_len + 1):
        for j in range(1, sentence2_len + 1):
            delta = 0 if sentence1[i - 1] == sentence2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j - 1] + delta, min(dp[i - 1][j] + 1, dp[i][j - 1] + 1))
    return dp[sentence1_len][sentence2_len]


if __name__ == "__main__":
    """编辑距离"""
    sentence1 = 'abc'
    sentence2 = 'bd'
    print(calculate_levenshtein_edit_distance(sentence1, sentence2))  # 2.0
    sentence1 = 'fxy'
    sentence2 = 'fab'
    print(calculate_levenshtein_edit_distance(sentence1, sentence2))  # 2.0
