# coding:utf-8

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def generate_wordcloud(text):
    '''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
    # 设置显示方式
    d=path.dirname(__file__)
    font_path=path.join(d,"font//msyh.ttf")
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white",# 设置背景颜色
           max_words=2000, # 词云显示的最大词数
           stopwords=stopwords, # 设置停用词
           font_path=font_path, # 兼容中文字体，不然中文会显示乱码
                   width=300,
                   height=200
                  )

    # 生成词云 
    wc.generate(text)

    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, "img//img1.png"))

