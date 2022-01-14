from colony import *
from collections import Counter
import time


class World:
    @staticmethod
    def __getarg(mas, fr):   # функция возвращает крайние значения для формирования рамок дисплея
        if len(mas) != 0:
            maxy, maxx = mas[0]
            miny, minx = mas[0]
            for i in mas:
                if i[0] > maxx:
                    maxx = i[0]
                if i[1] > maxy:
                    maxy = i[1]
                if i[0] < minx:
                    minx = i[0]
                if i[1] < miny:
                    miny = i[1]
            return max(maxx+fr, 10), max(maxy+fr, 10), min(minx-fr, 0), min(miny-fr, 0)
        else:
            return 10, 10, 0, 0

    def __init__(self, New_word, n=10, frames=1, pause=0.2):
        self.__frames = frames  # какое расстояние нужно до крайних значений живых клеток
        self.__arg = self.__getarg(New_word, self.__frames)  # tuple с крайними значениями
        self.__alive = {x for x in New_word}  # множество с живыми клетками
        self.__world = []
        self.__create()
        self.__New_Gen(n, pause)

    def __create(self):  # печатает в консоли дисплей игры
        self.__world = []
        for y in range(self.__arg[0]+1, self.__arg[2], -1):
            for x in range(self.__arg[3], self.__arg[1]+1):
                if (x, y) in self.__alive:
                    print('0', end=' ')
                else:
                    print('.', end=' ')
                self.__world.append(Cell(x, y, live=((x, y) in self.__alive)))
            print()

    def __New_Gen(self, n, pause):  # создаёт новую итерацию
        for j in range(1, n+1):
            time.sleep(pause)
            print('_'*(self.__arg[0] - self.__arg[2])*2)
            neighbor_count = []
            for i in self.__world:
                if i.is_alive:
                    neighbor_count.extend((x for x in i.neighbors()))
            neighbor_count = Counter(neighbor_count)
            Next_gen = [cell for cell in neighbor_count if (neighbor_count[cell] == 3) or
                        neighbor_count[cell] == 2 and cell in self.__alive]
            self.__arg = self.__getarg(Next_gen, self.__frames)
            self.__alive = {x for x in Next_gen}
            self.__create()
