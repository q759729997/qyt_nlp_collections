# 文本相似度

## 参考资料

- [邱锡鹏 文本数据管理与分析] <https://textprocessing.github.io/>
- [邱锡鹏 文本表示与相似度] <https://textprocessing.github.io/ch3.pdf>

## 编辑距离

- **描述：** 给定两个字符串a，b。编辑距离是将a转换为b的最少操作次数。
- **Levenshtein距离** 是编辑距离的一种，允许的操作包括一个字符替换成另一个字符，插入一个字符，删除一个字符。
- 参考资料：[详解编辑距离(Edit Distance)及其代码实现] <https://www.jianshu.com/p/a617d20162cf>
- [示例代码](./edit_distance.py)

## Jaccard相似度

- **描述：** 计算两个集合的相似度。J(X,Y) = |X∩Y| / |X∪Y|
- **Jaccard距离：** D(X,Y) = 1 – J(X,Y)
- 参考资料：[python实现——Jaccard相似度（jaccard_coefficient] <https://blog.csdn.net/bensonrachel/article/details/86434860>
- [示例代码](./jaccard_distance.py)
