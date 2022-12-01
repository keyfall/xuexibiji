import os
import datetime
from time import strftime
import shutil

# 根据艾宾浩斯记忆曲线，把文档日期在1,2,4,7,15天的文件存放到复习文件夹中,每天早上进行复习

file_address = "D:\学习笔记\日记"
target_address = file_address+"\复习"

def change_day(d):
    ld = d.split('.')
    if 10 > int(ld[0]):
        ld[0]=ld[0][-1]
    if 10 > int(ld[1]):
        ld[1] = ld[1][-1]
    return '.'.join(ld)

now = datetime.datetime.now()
all_files = os.listdir(file_address)



one = change_day((now - datetime.timedelta(days=1)).strftime("%m.%d"))+'.docx'
two = change_day((now - datetime.timedelta(days=2)).strftime("%m.%d"))+'.docx'
four = change_day((now - datetime.timedelta(days=4)).strftime("%m.%d"))+'.docx'
seven = change_day((now - datetime.timedelta(days=7)).strftime("%m.%d"))+'.docx'
fifteen = change_day((now - datetime.timedelta(days=15)).strftime("%m.%d"))+'.docx'


files = [one,two,four,seven,fifteen]

for x in iter(files):
    if x in all_files:
        os.makedirs(target_address, exist_ok=True)
        shutil.copy(file_address+'\\'+x,target_address)








