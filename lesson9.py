if __name__ == '__main__':

    # task 1
    # Write a function called oops that explicitly raises an IndexError exception when called.
    # Then write another function that calls oops inside a try/except statement to catch the error.
    def opps():
        raise IndexError
        # raise KeyError
    def oop_2():
        try:
            opps()
        except IndexError:
            print('IndexError exception')
        except KeyError:
            print('KeyError exception')

    oop_2()

    # task 2
    def mathematic():
        try:
            a = int(input('Write first number: a = '))
            b = int(input('Write second number: b = '))
            c = a ** 2 / b
            print(c)
        except ValueError:
            print('invalid literal')
        except ZeroDivisionError:
            print('division by zero')

    mathematic()

    # Напишите функцию которая будет переводить возраст с Земного на Марсианский.
    # В году на Земле 365 дней а на марсе 687
    def mars_age(age):
        age_mars = age * 365 // 687
        print(age_mars)
    try:
        a = int(input('Write Earth age for convert in Mars: '))
        mars_age(a)
    except ValueError:
        print('Only digits')


    # Напишите функцию greet принимающую имя name (type:str) м слово word (type:str).
    # Если слово не передано то считать его " -" и возвращающую строку вида "[Имя] ты сегодня [слово]!"
    def greet(name, word):
        if word == '':
            word = '-'
        print(f'{name}, ты сегодня {word}!')
    a = input('Напишите свое имя: ')
    b = input('Напишите слово: ')
    greet(a, b)

    # Напишите функцию joinA которая принимает неограниченное количество значений любого типа и
    # возвращает строку где эти значения склеены через символ A
    def joinA(*kwargs):
        return 'A'.join([str(x) for x in kwargs])
    print(joinA('hello', 123, True))
