# task1: task School
class Person:

    def __init__(self, name, age, sex, hob):
        self.name = name
        self.age = age
        self.sex = sex
        self.hob = hob

    def hobby(self, hob=''):
        self.hob = hob

class Student(Person):
    def __init__(self, name, age, sex, hob, course):
        super(Student, self).__init__(name, age, sex, hob)
        self.course = course

    def sudent_course(self, course):
        self.course = course

    def general(self):
        return f'Name: {self.name}; Age:{self.age}; Sex:{self.sex}; Hobby:{self.hob}; Course:{self.course}'

class Teacher(Person):

    def __init__(self, name, age, sex, hob, money):
        super(Teacher, self).__init__(name, age, sex, hob,)
        self.money = money

    def selary(self, money):
        self.money = money

    def general(self):
        return f'Name: {self.name}; Age:{self.age}; Sex:{self.sex}; Hobby:{self.hob}; Salary:{self.money}'

# task2: Mathematician
class Mathematician:

    def square_nums(self, *args):
        return [i**2 for i in args]

    def remove_positives(self, *args):
        return [i for i in args if i < 0]

    def filter_leaps(self, *args):
        return [i for i in args if i % 400 == 0 or i % 100 != 0 and i % 4 == 0]

# task3: Product

class Product:

    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductInShop:
    def __int__(self, prod):
        self.prod = prod
        self.amount = 0
        self.price = prod.price


class ProductStore:
    def __init__(self, prod):
        self.prod = prod
        self.products = []

    def add(self, product, amount):
        self.prod = product
        product.amount = amount
        self.products.append(product)

    def set_discount(self, identifier, percent):
        for product in self.products:
            if product.name == identifier:
                product.price = product.price - (product.price * percent / 100)
                print(product.price)

    def sell_product(self, pr, amount):
        for product in self.products:
            if product.name == pr:
                if product.amount > amount:
                    product.amount -= amount
                    print(product.amount)
                elif product.amount == amount:
                    print('All product was sold out')

    def get_all_products(self):
        all_products = []
        for p in self.products:
            all_products.append({'Type':self.prod.type, 'Name':self.prod.name, 'Amount':self.prod.amount})
        print(all_products)

    def get_products_info(self, name):
        for product in self.products:
            if product.name == name:
                print(self.prod.name, self.prod.amount)


if __name__ == '__main__':
   person = Student('Tanya', 24,'female', 'yoga', 'Python')
   print(person.general())
   person2 = Teacher('Ann', 43, 'female','', 200)
   print(person2.general())

   m = Mathematician()
   print(m.square_nums(2, 5, 8))
   print(m.remove_positives(-8, 9, 7))
   print(m.filter_leaps(1997, 2020))

   p1 = Product('food', 'ramen', 100)
   p2 = Product('food', 'bread', 15)
   sp = ProductStore(p1)
   sp.add(p1, 10)
   sp.add(p2, 10)
   sp.get_all_products()
   sp.set_discount('bread', 10)
   sp.sell_product('bread', 10)
   sp.get_products_info('ramen')