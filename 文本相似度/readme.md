# 文本相似度

## 参考资料

- [邱锡鹏 文本数据管理与分析] <https://textprocessing.github.io/>
- [邱锡鹏 文本表示与相似度] <https://textprocessing.github.io/ch3.pdf>

## 基于符号表示的相似度

### 编辑距离

- **描述：** 给定两个字符串a，b。编辑距离是将a转换为b的最少操作次数。
- **Levenshtein距离** 是编辑距离的一种，允许的操作包括一个字符替换成另一个字符，插入一个字符，删除一个字符。
- 参考资料：[详解编辑距离(Edit Distance)及其代码实现] <https://www.jianshu.com/p/a617d20162cf>
- [示例代码 edit_distance.py](./edit_distance.py)
- [示例代码 edit_distance_nltk.py](./edit_distance_nltk.py)

### Jaccard相似度

- **描述：** 计算两个集合的相似度。J(X,Y) = |X∩Y| / |X∪Y|
- **Jaccard距离：** D(X,Y) = 1 – J(X,Y)
- 参考资料：[python实现——Jaccard相似度（jaccard_coefficient] <https://blog.csdn.net/bensonrachel/article/details/86434860>
- [示例代码 jaccard_distance.py](./jaccard_distance.py)
- [示例代码 jaccard_distance_nltk.py](./jaccard_distance_nltk.py)

## 基于向量的相似度

### Cosine相似度

- **描述：** 两个向量的夹角。K(X, Y) = <X, Y> / (||X||*||Y||)
- **Cosine距离：** = 1 – Cosine相似度
- 参考资料：[Python Numpy计算各类距离] <https://blog.csdn.net/qq_19707521/article/details/78479532>
- [示例代码 cosine_distance.py](./cosine_distance.py)
- [示例代码 cosine_distance_sklearn.py](./cosine_distance_sklearn.py)
