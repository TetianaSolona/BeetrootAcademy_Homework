# binary search
def binary_search(data, element):
    if len(data) == 0:
        return False
    else:
        middle = len(data) // 2
        if data[middle] == element:
            return True
        elif element > middle:
            return binary_search(data[middle + 1:], element)

        else:
            return binary_search(data[:middle], element)


# fibonachi search
def fibonachi_search(data: list, element: int):
    length = len(data)
    index = -1
    x0 = 0
    x1 = 1
    x2 = 1
    while x2 < length:
        x0 = x1
        x1 = x2
        x2 = x1 + x0
    while x2 > 1:
        index = min(index + x0, length - 1)
        if data[index] < element:
            x2, x1 = x1, x0
            x0 = x2 - x1

        elif data[index] > element:
            x2 = x0
            x1 = x1 - x0
            x0 = x2 - x1
        else:
            return index
    if x1 and (data[index + 1] == element):
        return index + 1


if __name__ == '__main__':
    list = [23, 5, 78, 44, 1, 11, 16, 90]
    print(binary_search(list, 90))
    print(fibonachi_search([34, 1, 88, 99, 3, 56, 8], 3))
