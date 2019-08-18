# 文本表示与统计

## 参考资料

- [邱锡鹏 文本数据管理与分析] <https://textprocessing.github.io/>
- [邱锡鹏 文本表示与相似度] <https://textprocessing.github.io/ch3.pdf>

## TF-IDF

- **词频（term frequency，TF）：** 指的是某一个给定的词语在该文档中出现的频率。
- **逆向文档频率（inverse document frequency， IDF）：** 是一个词语普遍重要性的度量。某一个特定词语的IDF，可以由总文档数目除以包含该词语之文件的数目，再将得到的商取对数得到。idf(d, t) = log [ n / (df(d, t) + 1) ]
- **TF-IDF** 𝑤(𝑡, 𝑑) = 𝑇𝐹(𝑡, 𝑑) × 𝐼𝐷𝐹(𝑡)
- [概念解析:] <https://devdocs.io/scikit_learn/modules/generated/sklearn.feature_extraction.text.tfidftransformer#sklearn.feature_extraction.text.TfidfTransformer>
- 参考资料：[TF-IDF的算法Python实现和简单示例] <https://zhuanlan.zhihu.com/p/26766008>
- [示例代码 tf_idf.py](./tf_idf.py)
- [示例代码 tf_idf_sklearn.py](./tf_idf_sklearn.py)
