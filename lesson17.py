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
my_list = [x*x for x in range(1,10)]
my_generator = (x*x for x in range(1,10))


if __name__ == '__main__':
    print(list(with_index(['Cristmas', 'New Year'])))
    print(list(in_range(2,16,2)))

    print(my_list)
    for x in my_generator:
        print(x)
