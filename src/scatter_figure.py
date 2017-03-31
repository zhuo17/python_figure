# -*- coding: UTF-8 -*-
import csv
import io
import random
from matplotlib import pyplot as plt

# 解决绘图时，图标上的中文乱码问题
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

#  默认的模式是'rt'（文本可读）


def location(value):
    if value == "0":
        return random.uniform(0, 1)
    elif value == "1":
        return random.uniform(1, 2)
    elif value == "2":
        return random.uniform(2, 3)
    else:
        return value


def readfile(file_path, code, item):
    # 文件名解码decode
    # 'C:/Users/USER/Desktop/装瓶厂.csv'
    with io.open(file_path.decode(code), 'rb') as f:
        try:
            b = []
            reader = csv.DictReader(f)  # 以字典方式读取数据
            for column in reader:
                a = list()
                a.append(location(column[item]))
                a.append(location(column['label_cor']))
                a.append(location(column['label_dis']))
                b.append(a)

            plt.figure(figsize=(12, 8))
            plt.grid(color='b', linewidth='0.3', linestyle='--')  # 网格线
            plt.xlim(xmax=3, xmin=0)
            plt.ylim(ymax=3, ymin=0)
            plt.title(item + "散点图".decode(code))  # 注意中文乱码问题,字符串拼接
            plt.xlabel("x轴".decode(code))  # x轴标注
            plt.ylabel("y轴".decode(code))  # y轴标注
            for i in range(len(b)):
                for j in range(len(b[i])):
                    plt.plot(b[i][1], b[i][2], 'ro')  # ro:圆点
                    # plt.annotate(b[i][0].decode("utf-8"), xy=(b[i][1], b[i][2]), xytext=(b[i][1]-0.1, b[i][2]))
                    plt.text(b[i][1] - 0.1, b[i][2], b[i][0].decode(code))

            plt.show()

        finally:
            f.close()


readfile('C:/Users/USER/Desktop/bottler_cor_dis.csv', 'utf-8', 'bottler')
# readfile('C:/Users/USER/Desktop/channel_cor_dis.csv', 'utf-8', 'channel')  # 注意源文件的编码
# readfile('C:/Users/USER/Desktop/kpi_cor_dis.csv', 'utf-8', 'kpi')



