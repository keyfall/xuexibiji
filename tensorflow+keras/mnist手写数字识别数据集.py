import matplotlib.pyplot as plt
from keras.datasets import mnist

(X_train_image, y_train_label), (X_test_image, y_test_label) = mnist.load_data()

#查看多项训练数据images与label
def plot_images_l(images, labels, prediction, idx, num=10):
    #设置显示图形大小
    fig = plt.gcf()
    fig.set_size_inches(12,14)

    if num>25:  num=25
    for i in range(0, num):
        #建立subgraph字图形为5行5列
        ax = plt.subplot(5,5,1+i)
        #显示图形，参数是28*28的图形，binary是以黑白灰度显示
        ax.imshow(images[idx], cmap='binary')
        title = "label=" +str(labels[idx])
        if len(prediction)>0:
            title+=',predict='+str(prediction[idx])
        #设置标题
        ax.set_title(title,fontsize=20)
        #设置不显示刻度
        ax.set_xticks([])
        ax.set_yticks([])
        idx+=1
    plt.show()

plot_images_l(X_train_image,y_train_label,[],0,30)


#多层感知器模型数据预处理
#建立多层感知器模型，先将images和label的内容进行预处理，才能使用多层感知器模型进行训练与预测
#数据预处理，将28*28的图形以reshape转换为一维向量,并且转换为float，用于后面的数字标准化
a = X_train_image.reshape(60000, 784).astype('float32')
#数字标准化，把数据压缩到一个区间里，比如这里每个数字都是0到255，那么除以255就压缩到0-1了，这也是为什么要转换成float，否则结果应该就是0或者1
a/255


