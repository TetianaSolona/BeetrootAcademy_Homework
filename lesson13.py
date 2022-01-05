# task 1

class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def talk(self):
        print('Meow')

class Dog(Animal):
    def talk(self):
        print('Wow')

# task 2
class Library:

    def __init__(self, name):
        self.name = name
        self.__books = []
        self.__authors = []

    @property
    def books(self):
        return self.__books

    @property
    def author(self):
        return self.__authors

    def new_book(self, b: 'Book'):
        if b not in self.books:
            self.books.append(b)
        return self.books

    def group_by_year(self, year):
        books = []
        for book in self.books:
            if book.year == year:
                books.append(book)
        return books

    def group_by_author(self, author):
        authors = []
        for auth in self.authors:
            if auth.name == author:
                authors.append(auth)
        return authors

    def __repr__(self):
        return 'Name:' + self.name + ' ' + 'Books:' + str(self.books)

    def __str__(self):
        return self.__repr__()


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.__books = []

    @property
    def book(self):
        return self.__books

    def create_new_book(self, name='', year=None):
        b = Book(name=name, year=year, author=self)
        if b not in self.__books:
            self.__books.append(b)
            return b

    def __repr__(self):
        return self.name + ' ' + self.country + ' ' + str(self.birthday)

    def __str__(self):
        return self.__repr__()


class Book:
    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return 'Book:' + self.name + ' ' + str(self.year) + ' ' + 'Author:' + str(self.author) + '\n'

    def __str__(self):
        return self.__repr__()


# task 3
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, numerator=0, denomirator=1):
        if denomirator == 0:
            raise ZeroDivisionError('Denominator cannot be zero')
        self.numerator = numerator
        self.denominator = denomirator

    def __add__(self, other):
        new_num = self.numerator * other.denominator + self.denominator * other.numerator
        new_den = self.denominator * other.denominator
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __sub__(self, other):
        new_num = self.numerator * other.denominator - self.denominator * other.numerator
        new_den = self.denominator * other.denominator
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __mul__(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other):
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        return (self.numerator == other.numerator and self.denominator == other.denominator)

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)


if __name__ == '__main__':
    animals = [Cat('Garfild'), Dog('Sharik')]
    for animal in animals:
        animal.talk()

    author1 = Author('Тарас Шевченко', 'Україна', 1814)
    author2 = Author('Ліна Костенко', 'Україна', 1930)
    book1 = author1.create_new_book('Заповіт', 1845)
    book2 = author2.create_new_book('Маруся Чурай', 1979)
    library1 = Library('Міська бібліотека')
    library1.new_book(book1)
    library1.new_book(book2)
    print(library1)


    f1 = Fraction(2, 7)
    f2 = Fraction(2, 4)
    f3 = f1 / f2
    print(f3)
    print(f1 == f2)
