# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
import os
import requests
import json
import random
from threading import Thread
import time
import tkinter
import tkinter.messagebox


def haircut():  # 滚筒显示
    contend = "猪猪天下第一,万岁万岁....."
    while True:
        #     os.system('cls')
        print(contend)
        time.sleep(0.2)
        contend = contend[1::] + contend[0]


def generate_code(bit=4):  # 生产随机验证码
    cum = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    a = ''
    for _ in range(0, bit):
        index = random.randint(0, len(cum) - 1)
        a += cum[index]
    return a


def get_web():
    resp = requests.get('http://api.tianapi.com/tiangou/index?key=86b96a99180d236d377d646b7c643347&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['content'])


class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age += age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def download_task(filename):
   # print('启动下载线程，线程号[%d].' % os.getpid())
    print('开始下载%s...' % filename)
    time_to_download = random.randint(5, 10)
    time.sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def download():
    # 模拟下载任务需要花费10秒钟时间
    time.sleep(3)
    tkinter.messagebox.showinfo('提示', '下载完成!')


def show_about():
    tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')


class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users//kuntang' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 通过requests模块的get函数获取网络资源
    # 下面的代码中使用了天行数据接口提供的网络API
    # 要使用该数据接口需要在天行数据的网站上注册
    # 然后用自己的Key替换掉下面代码的中APIKey即可
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=APIKey&num=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url).start()


if __name__ == '__main__':
    main()