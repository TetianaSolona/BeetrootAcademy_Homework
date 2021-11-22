if __name__ == '__main__':

    # task 1
    # String manipulation

    a = input()
    if len(a) > 2:
        print(a[0:2] + a[-2:])
    elif len(a) == 2:
        print(a * 2)
    else:
        print('Empty String')

    # task 2
    # The valid phone number program.

    a = input('Write your phone number:')
    if a.isdigit() and len(a) == 10:
        if a[:3] == '063' or a[:3] == '093' or a[:3] == '073':
            print('Your operator is Lifecell')
        elif a[:3] == '067' or a[:3] == '097':
            print('Your number is Kyivstar')
        elif a[:3] == '066' or a[:3] == '095' or a[:3] == '099':
            print('Your numer is Vodafon')
        else:
            print('You have unknown operator')
    else:
        print('Phone number is not correct')

    # task 3
    # name check

    name = 'tania'
    ask_name = input('What is your name?')
    if ask_name.lower() == name:
        print(True)
    else:
        print(False)

    # github
    # Допишите код так, чтобы меняя значение переменной day_of_week выводились следующие сообщения
    # ʼрабочий деньʼ, 'выходной', 'Ошибка! Дни недели считаются 1-7 ни больше ни меньше!'
    day_of_week = 4
    if 1 <= day_of_week <= 5:
        print('work day')
    elif day_of_week == 6 or day_of_week == 7:
        print('day off')
    else:
        print('mistake')

    # задание У вас есть переменные holiday, day_of_week, wallet
    # проставьте условия в код. попробуйте менять исходные значения чтоб убедиться что все работает
    holiday, day_of_week, wallet = True, 6, 5000
    if holiday and day_of_week == 6 and wallet == 0:
        print("оно то и можно погулять но не на что")
    elif holiday and day_of_week == 6 and wallet < 5000:
        print("пиво и чипсы на большее денег нет")
    elif holiday and day_of_week == 6 and wallet == 5000:
        print("гуляем в ресторане, всех угощаю")
    elif holiday and day_of_week == 6 and wallet > 5000:
        print("После Безоса следующим лечу я. И моя любимая кошка!")
    else:
        print("работаем")

    # задание Выведите значения у для х в пределах от 0 до 100 c шагом 1 если y = 3x + 12
    x = 0
    while x <= 100:
        print('y =', 3 * x + 12)
        x += 1

    # задание
    question = input('Маленькое беленькое на потолко висит не светит')
    answer = 'лампачка'
    i = 1
    while question != answer:
        if question == 'q' or question == 'Q':
            print('провал')
            break
        question = input('Маленькое беленькое на потолко висит не светит')
    else:
        print('поздравляю')

    # мобильный оператор
    a = input('здравствуй, если хочешь узнать акции нажми 1, если тариф 2, если погоду 3')
    while True:
        if a == '2':
            b = input('узнать свой тариф 1, новые тарифы 2, остаток по счету 3')
            print(b)
            if b == '1':
                print('ваш тариф Лайф+')
            elif b == '2':
                print('новый тариф Лайф2+')
            elif b == 3:
                print('на вашем счете 3 грн')
            break
        elif a == '1':
            print('обменяй бонусы на звонки')
        elif a == '3':
            print('сегодня +1 градус, солнечно')
        elif a == 'q':
            print('будем ждать ващего запроса')
            break
        break
