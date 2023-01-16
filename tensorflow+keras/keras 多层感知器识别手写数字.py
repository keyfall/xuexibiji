# 1.数据预处理:数据预处理后，会产生features(数字图像特征值)与label(数字真实的值)
# 2.建立模型:建立多层感知器模型
# 3.训练模型:输入训练数据feature与label,进行10次训练
# 4.评估模型准确率,使用测试数据评估模型准确率
# 5.进行预测:使用已经训练完成的模型，输入测试数据进行预测
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Dropout
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(10)
(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()

#将features使用reshape转换并且数字标准化
x_Train_normalize = x_train_image.reshape(60000,784).astype('float32')/255
x_Test_normalize = x_test_image.reshape(10000, 784).astype('float32')/255

#使用np_utils.to_categorical将训练数据与测试数据的label进行One-Hot Encoding转换
#one-hot讲解：https://www.imooc.com/article/35900
y_Train_OneHot = np_utils.to_categorical(y_train_label)
y_Test_OneHot = np_utils.to_categorical(y_test_label)

#容器描述了神经网络的网络结构，在Sequential()的输入参数中描述从输入层到输出层的网络结构
model = Sequential()
#units隐藏层256，input_dim输入层784
#kernel_initializer使用normal distribution正态分布的随机数初始化weith,bias
#activation，定义激活函数为relu，激活函数感觉就是把输入的值通过激活函数变为输出值，然后根据训练数据调校里面的内容
model.add(Dense(units=1000,
                input_dim=784,
                kernel_initializer='normal',
                activation='relu'))
#增加Dropout模块，主要功能降低过拟合，可以增加一些准确率
model.add(Dropout(0.5))

#再加入一个隐藏层2和一个dropout
model.add(Dense(units=1000,
                kernel_initializer='normal',
                activation='relu'))
model.add(Dropout(0.5))
#这里input_dim会按照上层的units为256自动设置
model.add(Dense(units=10,
                kernel_initializer='normal',
                activation='softmax'))

#输出model的信息，param运算公式256*10+10
print(model.summary())

#对训练模型进行设置
#loss损失函数,categorical_crossentropy是交叉熵，介绍：https://blog.csdn.net/Z99999888/article/details/101471784
#optimizer，优化器，adam可以让训练更快收敛，提高准确率
#metrics，设置评估模型的方式是准确率
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#执行训练
#validation_sqlit设置训练和验证数据比例，80%作为训练数据
#epochs训练周期，batch_size每一批次200数据，verbose显示训练过程
train_history = model.fit(x=x_Train_normalize,
                          y=y_Train_OneHot,
                          validation_split=0.2,
                          epochs=10,
                          batch_size=200,
                          verbose=2)

#画图，根据每一次训练数据和验证数据的显示结果看出训练数据和验证数据的准确率和接近
def show_train_history(train_history,train,validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()

show_train_history(train_history,'accuracy','val_accuracy')


#evaluate评估模型的准确率
sources = model.evaluate(x_Test_normalize, y_Test_OneHot)
print()
print('accuracy=', sources)

#通过test数值进行预测，得到测试结果
prediction=model.predict(x_text_image.reshape(10000,784).astype('float32'))
pre = np.argmax(prediction,axis=1)

#展示图片和实际值与预测值
def plot_images_l(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12,14)
    if num>25:  num=25
    for i in range(0, num):
        ax = plt.subplot(5,5,1+i)
        ax.imshow(images[idx], cmap='binary')
        title = "label=" +str(labels[idx])
        if len(prediction)>0:
            title+=',predict='+str(prediction[idx])
        ax.set_title(title,fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx+=1
    plt.show()
plot_images_l(x_test_image,y_test_label,pre,idx=340)



#pandas.crosstab建立混淆矩阵，用来了解哪些数据准确率高，哪些准确率低的
pd.crosstab(y_test_label,pre,rownames=['label'],colnames=['predict'])

#通过dataFrame找到错误的数据
df = pd.DataFrame({'label':y_test_label, 'predict':pre})
df[(df.label==5)&(df.predict==3)]
plot_images_l(x_test_image,y_test_label,pre,idx=5982,num=1)