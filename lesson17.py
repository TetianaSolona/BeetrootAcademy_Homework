# task 1
def with_index(iterable, start=0):
    for iter in iterable:
        yield start, iter
        start += 1

# task 2
def in_range(start, end, step=1):
    while start <= end:
        yield start
        start += step

# task 3
class MyIter:
    def __init__(self, args):
        self.__index = 0
        self.__data = args

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__data):
            raise StopIteration
        answer = self.__data[self.__index]
        self.__index += 1
        return answer

    def __getitem__(self, item):
        return self.__data[item]


if __name__ == '__main__':
    print(list(with_index(['Cristmas', 'New Year'])))
    print(list(in_range(2,16,2)))

    it = MyIter('12345')
    for i in it:
        print(i)
    print(it.__getitem__(2))
