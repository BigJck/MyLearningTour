def main():
    try:
        file1 = open('/Users/kuntang/.ssh/id_rsa (997406763@qq.com)', 'r')
        data = file1.read()
        print(type(data))
        print(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开.')
    except IOError as e:
        print('读写文件时出现错误.')
    finally:
        file1.close()


if __name__ == '__main__':
    main()