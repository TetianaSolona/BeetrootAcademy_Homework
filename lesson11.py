if __name__ == '__main__':

    # task 1
    # Make a class called Person. Make the __init__() method take firstname,
    # lastname, and age as parameters and add them as attributes. Make another method called talk()
    # which makes prints a greeting from the person containing,
    # for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

    class Person:
        def __init__(self, name, lastname, age):
            self.name = name
            self.lastname = lastname
            self.age = age

        def greeting(self):
            print(f'Hello, my name is {self.name} {self.lastname} and I`m {self.age} years old.')

    ones = Person('Carl', 'Johnson', 26)
    ones.greeting()

    # task 2
    # Create a class Dog with class attribute `age_factor` equals to 7.
    # Make __init__() which takes values for a dog’s age.
    # Then create a method `human_age` which returns the dog’s age in human equivalent.

    class Dog:
        age_factor = 7

        def __init__(self, dog_age):
            self.dog_age = dog_age

        def human_age(self):
            return self.dog_age * self.age_factor

    dog = Dog(3)
    print(dog.human_age())

    # task 3
    # TV controller
    CHANNELS = ['BBC', 'Discovery', 'TV1000']

    class TVController:

        def __init__(self, channel):
            self.channel = channel[:]
            self.current_channel = self.channel[0]

        def first_channel(self):
            self.current_channel = self.channel[0]
            return self.current_channel

        def last_channel(self):
            self.current_channel = self.channel[-1]
            return self.current_channel

        def turn_channel(self, num):
            self.current_channel = num % len(self.channel)
            return self.current_channel

        def previous_channel(self):
            return self.current_channel % len(self.channel) - 1

        def next_channel(self):
            if self.channel.index(self.current_channel) == len(self.channel) - 1:
                self.current_channel = self.channel[0]
            else:
                self.current_channel = self.channel[self.channel.index(self.current_chanel) + 1]
            return self.current_channel

        def cur_channel(self):
            return self.current_channel

        def exist_channel(self, num):
            for number, name in enumerate(self.channel):
                if num == number + 1 or num == name:
                    return 'Exist'
                else:
                    return 'No exist'


    controller = TVController(CHANNELS)
    print(controller.first_channel())
    print(controller.last_channel())
    print(controller.next_channel())
    print(controller.turn_channel(2))
    print(controller.previous_channel())
    print(controller.cur_channel())
    print(controller.exist_channel(2))

    # Создайте класс Friend для хранения имени name и телефона phone.
    # Обратите внимание, у друга может не быть телефона.
    class Friend:

        def __init__(self, name, phone=''):
            self.name = name
            self.phone = phone

    u1 = Friend('Andrew', '0999998888')
    u2 = Friend('Ann')
    print(u1.name)
    print(u1.phone)
    print(u2.name)
    print(u2.phone)

    # Буква А
    class SymbolA:

        def __init__(self, symbol):
            self.symbol = symbol

        def draw(self):
            return f'{self.symbol*3}\n{self.symbol}  {self.symbol}\n{self.symbol*4}\n{self.symbol}  {self.symbol}'

        def lin(self, number):
            line = self.draw().split('\n')
            return line[number + 1]

    a = SymbolA('#')
    print(a.draw())
    print(a.lin(2))
