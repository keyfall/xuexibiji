import os
import datetime
from time import strftime
import shutil

# 根据艾宾浩斯记忆曲线，把文档日期在1,2,4,7,15天的文件存放到复习文件夹中,每天早上进行复习

# 输入数字,来实现几天没有学习，算实际复习日期=当前日期-几天空闲
def delay_days_process(point_for_input):
    delay_days = input(point_for_input)
    if not delay_days:
        return 0
    if not delay_days.isdigit():
        delay_days = delay_days_process("输入数字:")
    return int(delay_days)


delay_days = delay_days_process("你丫几天没学习了（输入天数）:")


now = datetime.datetime.now() - datetime.timedelta(days=delay_days)



file_address = "D:\学习笔记\日记"
target_address = file_address+"\复习"


all_files = os.listdir(file_address)

#删除昨天生成的目录
if os.path.exists(target_address):
    shutil.rmtree(target_address)



one = (now - datetime.timedelta(days=1)).strftime("%m.%d")
two = (now - datetime.timedelta(days=2)).strftime("%m.%d")
four = (now - datetime.timedelta(days=4)).strftime("%m.%d")
seven = (now - datetime.timedelta(days=7)).strftime("%m.%d")
fifteen = (now - datetime.timedelta(days=15)).strftime("%m.%d")
onemonth = (now - datetime.timedelta(days=30)).strftime("%m.%d")
fourtyfive = (now - datetime.timedelta(days=45)).strftime("%m.%d")
sixty = (now - datetime.timedelta(days=60)).strftime("%m.%d")


files = [one,two,four,seven,fifteen,onemonth,fourtyfive,sixty]

#遍历文件修改日期，然后和对应的天数生成的日期进行对比，符合就新建目录，copy文件进去
for x in iter(all_files):
    if datetime.datetime.fromtimestamp(os.path.getmtime(file_address+'\\'+x)).strftime("%m.%d") in files:
        os.makedirs(target_address, exist_ok=True)
        shutil.copy(file_address+'\\'+x,target_address)








