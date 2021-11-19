if __name__ == '__main__':
    # задание 1.0
    total = 44
    rez = int(44 * 0.8)
    print("Для успешного окончания курса надо сдать {} домашек".format(rez))

    # координаты
    x1 = 0
    y1 = 0
    x2 = 6
    y2 = 7
    print(int(((x2-x1)**2+(y2-y1)**2)**0.5))

    #
    height = 30
    width = 10
    lenght = 10
    size = 3 * 4
    price = 600

    squares = ((width ** 2 + lenght ** 2)**0.5) * height
    amount = int(squares / size + 1)
    summa = int(amount * price)
    res = int(squares % size)
    print(amount, summa, res)

    #
    var1 = 'pyThoN'
    var1.lower()
    print(var1.capitalize())
    print(var1.upper())
    print(var1.lower())
    var1 = " python "
    print(var1.strip())

    # Задача на форматирование вывода
    name = 'Tanya'
    print('Hello, {}'.format(name))
    print(f'Hello, {name}')
    print('Hello, %s' % name)

    # Задача
    price = 12
    weight = 3.4121
    rez = price * weight
    rez = 'Итого: %.2f' % rez
    print(rez)

    # Задача
    number = bin(12)
    username = "ираклий"
    access_mask = bin(54)
    hour_price = '%.2f' % 15.321
    rez = f'{number} {username} {access_mask} {hour_price}'
    print(rez)

    # Задача
    base_str = 'Корова'
    rez = base_str[1:-2]
    rez = 'В' + rez + 'на'
    print(rez)

    # Задача
    a = 10
    b = 55
    a, b = b, a
    print(a, b)

    # задание с картинкой
    x = 12
    a = 34
    y0 = ((2 + (x / a)) ** 3) / ((x ** 2 + 4 * (a ** 2) + 4 * a * x) / (8 * (a ** 3)))
    y1 = 8 * (2 * a + x)
    y2 = 8 / (x + 2 * a)
    y3 = (x + 2 * a) / 8
    y4 = 1 / (8 * (x + 2 * a))
    print(y0, y1, y2, y3, y4)
