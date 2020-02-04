## 训练词向量

- 参考链接：<http://fasttext.apachecn.org/#/doc/zh/unsupervised-tutorials>
- 基于这个数据来学习词向量只需要一个命令就能实现：

~~~
$ mkdir result
$ ./fasttext skipgram -input data/fil9 -output result/fil9
解释这行命令： ./fastext 用 skipgram 模型（或者是 cbow 模型）调用 fastText 二进制的可执行文件（在这里参考如何安装 fastText ）。然后，'-input' 选项要求我们指定输入数据的位置，'-output' 指定输出要保存的位置。
~~~

- 示例训练命令

~~~
./fasttext skipgram -input /media/sf_vbshare/wordembedding/pku/pku-train.seg -output /media/sf_vbshare/wordembedding/pku/
~~~

- 当 fastText 运行时，屏幕上会显示进度和预计完成时间。一旦程序结束，result 目录中应该有两个文件：

~~~
$ ls -l result
-rw-r-r-- 1 bojanowski 1876110778 978480850 Dec 20 11:01 fil9.bin
-rw-r-r-- 1 bojanowski 1876110778 190004182 Dec 20 11:01 fil9.vec
fil9.bin 是一个二进制文件，用于存储整个 fastText 模型，并可以在之后重新加载。 fil9.vec 是一个包含词向量的文本文件，词汇表中的一个单词对应一行：
~~~

~~~
$ head -n 4 result/fil9.vec
218316 100
the -0.10363 -0.063669 0.032436 -0.040798 0.53749 0.00097867 0.10083 0.24829 ...
of -0.0083724 0.0059414 -0.046618 -0.072735 0.83007 0.038895 -0.13634 0.60063 ...
one 0.32731 0.044409 -0.46484 0.14716 0.7431 0.24684 -0.11301 0.51721 0.73262 ...
第一行说明了单词数量和向量维数。随后的行是词汇表中所有单词的词向量，按降序排列。
~~~

## 词向量使用

- 打印词向量

~~~
echo "北京 中国 日本" | ./fasttext print-word-vectors /media/sf_vbshare/wordembedding/pku/.bin
~~~

- 最近邻查询

~~~
./fasttext nn /media/sf_vbshare/wordembedding/pku/.bin
北京
江泽民
大学
~~~

- 字的类比

~~~
./fasttext analogies /media/sf_vbshare/wordembedding/pku/.bin
北京 中国 日本
江泽民 中国 美国
~~~