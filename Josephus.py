def jojo(human=30, kill=15, count_num=9):    # 总共人数，处死人数,数几次处死人
    people = [x for x in range(1, human+1)]   # 建立人数相等的列表 1表示人还活着
    now = 0
    dead_list = []
    for x in range(0, kill):
        for _ in range(0, count_num-1):
            now += 1
            now %= 30-x                   # 用列表构建循环队列的关键
        dead_list.append(people.pop(now))
    print('Deadpeople is ', end= '  ')
    print(dead_list)
    print('Alivepeople is ', end = ' ')
    print(people)






def main():

    jojo()


if __name__ == '__main__':
    main()