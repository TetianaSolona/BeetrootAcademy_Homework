import random


def merge_sort(lst: list[int])-> list[int]:
    if len(lst) <= 1:
        return lst
    midl = len(lst)//2
    left_sorted = merge_sort(lst[0:midl])
    righg_sorted = merge_sort(lst[midl:])
    sorted_list = []
    while left_sorted and righg_sorted:
        left = left_sorted.pop(0)
        righg = righg_sorted.pop(0)
        if left < righg:
            sorted_list.append(left)
            righg_sorted.insert(0, righg)
        elif righg < left:
            sorted_list.append(righg)
            left_sorted.insert(0, left)
        else:
            sorted_list.append(left)
            sorted_list.append(righg)
    sorted_list += left_sorted + righg_sorted
    return sorted_list

if __name__ == '__main__':
    l = [random.randint(5,20) for i in range(10)]
    print(l)
    print(merge_sort(l))


