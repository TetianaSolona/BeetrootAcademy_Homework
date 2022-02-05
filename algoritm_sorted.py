# bubble sorted

def bubble_sorted(data: list[int]) -> list[int]:
    flag = True
    index = len(data) - 1
    while index > 0 and flag:
        flag = False
        for i in range(index):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                flag = True
    return data


# merge sort
def merge_sorted(data: list[int]) -> list[int]:
    if len(data) <= 1:
        return data
    middle = len(data) // 2
    left = merge_sorted(data[:middle])
    right = merge_sorted(data[middle:])
    result = []
    i, j = 0, 0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result


# insertion sort
def insertion_sorted(data: list[int]) -> list[int]:
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
            data[j + 1] = key
    return data


if __name__ == '__main__':
    list = [23, 5, 6, 87, 99, 88]
    print(bubble_sorted(list))
    print(merge_sorted(list))
    print(insertion_sorted(list))

