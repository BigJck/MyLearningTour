from math import sqrt


class Points(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        dx = self.x-other.x
        dy = self.y-other.y
        return sqrt(dx**2 + dy**2)


def main():
    point1 = Points(3, 4)
    point2 = Points()
    print(point1.distance_to(point2))
    point2.move_to(10, 10)
    print(point1.distance_to(point2))


if __name__ == '__main__':
    main()
