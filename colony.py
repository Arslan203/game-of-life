class Cell:
    def __init__(self, x, y, live=False):
        self.__x = x
        self.__y = y
        self.__live = live

    def neighbors(self):
        return [(self.__x-1, self.__y-1), (self.__x, self.__y-1), (self.__x+1, self.__y-1),
                (self.__x-1, self.__y), (self.__x+1, self.__y),
                (self.__x-1, self.__y+1), (self.__x, self.__y+1), (self.__x+1, self.__y+1)]

    @property
    def is_alive(self):
        return self.__live
