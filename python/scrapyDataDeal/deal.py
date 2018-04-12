# coding=utf-8
__author__ = 'luoys'

from pymongo import MongoClient
import jieba
import pandas as pd
import numpy
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud  # 词云包


client = MongoClient('localhost', 27017)
db = client.mydb
collection = db.Comment

comments = ''
for item in collection.find({'artist_name': '陈奕迅'}):
    for i in xrange(10):
        str = item['comment_nice'][i][1]
        str = str[1:]
        if(str != None):
            comments = comments + str
print len(comments), comments

segment = jieba.lcut(comments)
words_df = pd.DataFrame({'segment': segment})

#去停用词
stopwords = pd.read_csv("chineseStopWords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'], encoding='gbk')  # quoting=3全不引
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]


words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)

print words_stat


wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80) #指定字体类型、字体大小和字体颜色

word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}

word_frequence_list = []

# for key in word_frequence:
#
#     temp = (key, word_frequence[key])
#
#     word_frequence_list.append(temp)

wordcloud_1 = wordcloud.fit_words(word_frequence)

# plt.imshow(wordcloud)
matplotlib.pyplot.imshow(wordcloud_1)
plt.axis("off")
plt.show()

#可以用的