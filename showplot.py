from os import path
import plotWordcloud
import chnSegment

def show():
    # 读取文件
    d = path.dirname(__file__)
    text = open(path.join(d, 'doc//countdata.txt'),encoding='gbk').read()
    # 若是中文文本，则先进行分词操作
    text = chnSegment.word_segment(text)
    # 生成词云
    plotWordcloud.generate_wordcloud(text)
    return plotWordcloud
# show()
