from math import atan
from math import sin
from math import sqrt


def main():
    print(atan(1)* 360 / 2 / 3.1415926)
    print(sin(atan(1/sqrt(3))))
    print(sin(3.1415926/6))


if __name__ == '__main__':
    main()
