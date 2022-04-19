import random


def show_num(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end = ' ')
        print('%02d' % ball, end = ' ')
    print()


def rand_sel():
    red_balls = [x for x in range(1, 34)]
    lucky_ball = random.sample(red_balls, 6)
    lucky_ball.append(random.randint(1, 17))
    return lucky_ball


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        show_num(rand_sel())


if __name__ == '__main__':
    main()