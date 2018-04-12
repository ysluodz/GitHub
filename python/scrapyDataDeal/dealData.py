#coding:utf-8
import warnings
from pymongo import MongoClient

warnings.filterwarnings("ignore")
import jieba    #分词包
import numpy    #numpy计算包
import codecs   #codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode
import re
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
from wordcloud import WordCloud#词云包


def main():

    client = MongoClient('localhost', 27017)
    db = client.mydb
    collection = db.Comment

    comments = ''
    for item in collection.find({'artist_name': '周杰伦'}):
        for i in xrange(10):
            str = item['comment_nice'][i][1]
            str = str[1:]
            if(str != None):
                comments = comments + str

    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)

    cleaned_comments = ''.join(filterdata)
    segment = jieba.lcut(cleaned_comments)

    words_df=pd.DataFrame({'segment':segment})

 

    #去掉停用词
    stopwords=pd.read_csv("chineseStopWords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='gbk') #quoting=3全不引用
    words_df=words_df[~words_df.segment.isin(stopwords.stopword)]

 

    #统计词频

    words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})

    words_stat=words_stat.reset_index().sort_values(by=["计数"],ascending=False)

 

    #用词云进行显示

    wordcloud=WordCloud(font_path="simhei.ttf",background_color="white",max_font_size=80)

    word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}

 

    word_frequence_list = []

    for key in word_frequence:

        temp = (key,word_frequence[key])

        word_frequence_list.append(temp)

 

    wordcloud=wordcloud.fit_words(word_frequence)
    # wordcloud = WordCloud(font_path = 'MSYH.TTF').fit_words(word_frequence)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
 

#主函数

main()