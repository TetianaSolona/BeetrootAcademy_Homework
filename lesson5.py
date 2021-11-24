import random

if __name__ == '__main__':

    # task 1
    # The Guessing Game
    a = input('Try to guess number from 1 to 10: ')
    print(random.randint(1, 10))
    b = random.randint(1, 10)
    b = str(b)
    if a == b:
        print('Congratulations! You are guess.')
    else:
        print('You will win next time)')

    # task 2
    # The birthday greeting program
    name = input('What`s your name?')
    age = int(input('How old are you?'))
    print(f'Hello {name}, on your next birthday you’ll be {age + 1} years!')

    # task 3
    string = input('Write word: ')
    count = 5
    lenght = 4
    word = ''
    while count > 0:
        count -= 1
        new_string = string
        word = ''
        while len(word) < lenght:
            index = random.randint(0, len(new_string)-1)
            word += new_string[index]
            new_string = string[:index] + string[index + 1:]
        print(word)

    # Task 4
    # The math quiz program
    a = input('Calculate this expression: y = 2x + 1, if x = 5: ')
    b = 2 * 5 + 1
    x = str(b)
    while a != b:
        if a == x:
            print('You are right')
            break
        if a == 'q':
            print('See you')
            break
        a = input('Calculate this expression: y = 2x + 1, if x = 5: ')
