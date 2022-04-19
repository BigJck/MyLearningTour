from abc import ABCMeta, abstractmethod


class Worker(object):
    __slots__ = '_name'

    def __init__(self, name):
        self._name = name

    @property
    def get_name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Worker):
    def get_salary(self):
        return 15000


class SDE(Worker):
    __slots__ = ('_name', '_hours')

    def __init__(self, name, hours=0):
        super().__init__(name)
        self._hours = hours

    def get_salary(self):
        return self._hours * 150


class Seller(Worker):
    __slots__ = ('_name', '_sell')

    def __int__(self, name, sell=0):
        super().__init__(name)
        self._sell = sell

    def get_salary(self):
        return self._sell * 0.05 + 1500


def main():
    mem_list = [Manager('Wang'), Manager('Lee'),
                 SDE('W', 50), SDE('F', 60), SDE('N', 70),
               # Seller('kk', 100), Seller('mm', 100)
                ]
    sum_salary = 0
    for x in mem_list:
        print(x.get_name, x.get_salary())
        sum_salary += x.get_salary()
    print('sum is %d' % sum_salary)


if __name__ == '__main__':
    main()
