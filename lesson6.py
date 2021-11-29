import random

if __name__ == '__main__':

    # Task 1. The greatest number
    lst = []
    lenght = 10
    while lenght > 0:
        lst.append(random.randint(0, 10))
        lenght -= 1
    print(lst)
    print(max(lst))

    # Task 2. Exclusive common numbers.
    list_1 = []
    list_2 = []
    lenght = 10
    while lenght > 0:
        list_1.append(random.randint(0, 10))
        list_2.append(random.randint(0, 10))
        lenght -= 1
        list_3 = list(set(list_1) | set(list_2))
    print(list_3)

    # Task 3. Extracting numbers.
    a = range(0, 100)
    new_a = []
    iteration = 0
    while iteration != 100:
        if a[iteration] % 7 == 0 and a[iteration] % 5 != 0:
            new_a.append(a[iteration])
        iteration += 1
    print(new_a)


    # Рандом и расширение списка.
    lst = []
    lenght = 10
    while lenght > 0:
        a = random.randint(0, 100)
        lst.append(a)
        lenght -= 1
    print('List:', lst)

    minimum = 100
    maximum = 0
    for i in lst:
        if minimum > i:
            minimum = i
        if maximum < i:
            maximum = i
    print('Minimum:', minimum)
    print('Maximum:', maximum)


    # Преобразование типов и слайсы.
    exmpl = "Привіт"
    exmpl = tuple(exmpl)
    var1 = ''.join(exmpl[::2])
    print(var1)
    assert var1 == "Пиі"


    # Сортировка и слайсы.

    gamer_list = []
    i = 0
    while True:
        gamer = input('Print name of gamer: ')
        i += 1
        if gamer == 'Q':
            break
        gamer_list.append(gamer)
    print(sorted(gamer_list))
    # не получается первого игрока соеденить с последним и так далее
    # i = 0
    # if len(gamer_list) / 2 == 0:
    #    while i < len(gamer_list):
    #        print(f'{gamer_list[i]} play with {gamer_list[-i-1]}')
    #        i += 1

    # Реверс.
    my_list = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    my_list.reverse()
    print(my_list)
