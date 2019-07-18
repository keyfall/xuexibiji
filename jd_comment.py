import requests
import os
import time
import json
import random

import jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# 评论数据保存文件
Comment_File_Path = 'jd_comment.txt'

# 词云形状图片
Wc_Mask_Img = './Documents/spider/wawa.jpg'
# 词云字体
Wc_Font_Path = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
def spider_comment(page=0):
    """
    爬取京东评论数据
    """

    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv2000&productId=100004918526&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1' % page
    kv = {'user-agent':'Mozilla/5.0', 'Referer':'https://item.jd.com/100004918526.html'}
    try:
        r = requests.get(url,headers=kv)
        #若有错误就none,正确就显示
        r.raise_for_status()
    except:
        print("爬取失败")
    # 获取json数据字符串
    r_json_str = r.text[26:-2]
    # print('京东评论数据:' + r_json_str[:500])
    
    # 字符串转json对象
    r_json_obj = json.loads(r_json_str)
    # 获取评价列表数据
    r_json_comments = r_json_obj['comments']
    print("评论数据")
    # 遍历评论对象列表
    for r_json_comment in r_json_comments:
        # 以追加模式换行写入每条评价
        with open(Comment_File_Path,'a+') as file:
            file.write(r_json_comment['content']+ '\n\r')
        # 获取评论对象中的评论内容
        print(r_json_comment['content'])

def batch_spider_comment():
    '''
    批量爬取京东评论
    '''
    #写入数据前先清空之前的数据
    if os.path.exists(Comment_File_Path):
        os.remove(Comment_File_Path)
    for i in range(100):
        spider_comment(i)
        # 设置时间间隔防止IP被封
        time.sleep(random.random()*5)

def cut_word():
    '''
    对数据分词
    '''
    with open(Comment_File_Path) as file:
        comment_txt = file.read()
        wordlist = jieba.cut(comment_txt, cut_all=True)
        wl = " ".join(wordlist)
        print(wl)
        return wl
def create_word_cloud():
    '''
    生成词云
    '''
    # 设置词云形状图片
    wc_mask = np.array(Image.open(Wc_Mask_Img))
    # 设置词云的一些配置,如:字体,背景色,词云形状,大小
    wc = WordCloud(background_color="white", max_words = 2000,
            mask=wc_mask,scale=4,max_font_size=50,
            random_state=42, font_path=Wc_Font_Path)
    # 生成词云
    wc.generate(cut_word())

    # 在只设置mask的情况下,得到一个拥有图片形状的词云
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()


if __name__=='__main__':
    create_word_cloud()
