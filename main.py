# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
import os
import random


def haircut():        # 滚筒显示
    contend = "猪猪天下第一,万岁万岁....."
    while True:
        #     os.system('cls')
        print(contend)
        time.sleep(0.2)
        contend = contend[1::] + contend[0]


def generate_code(bit=4):     # 生产随机验证码
    cum = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    a = ''
    for _ in range(0, bit):
        index = random.randint(0, len(cum)-1)
        a += cum[index]
    return a


def main():
    f = None
    try:
        f = open('/Users/kuntang/.ssh/id_rsa (997406763@qq.com)', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()