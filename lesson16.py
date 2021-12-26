import re

# task 1
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
class Validate:

    @staticmethod
    def validate_email(email):
        if (re.fullmatch(regex, email)):
            print("Valid Email")
        else:
            print("Invalid Email")

# task 2
class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def employ(self):
        return self.workers

    @employ.setter
    def add_worker(self, employee):
        if not employee.boss:
            self.workers.append(employee)

    @employ.deleter
    def del_worker(self, employee):
        if employee.boss:
            self.workers.remove(employee)


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    @property
    def my_boss(self):
        if not self.boss:
            return 'Don`t have boss'
        return self.boss


    @my_boss.setter
    def my_boss(self, boss):
        if not self.boss:
            self.boss = boss
            self.company = boss.company
            return 'Boss was add'

    @my_boss.deleter
    def my_boss(self):
        del self.boss
        del self.company

# task 3
class TypeDecorators:

    def to_int(self, func):
        def wrapper(*args, **kwargs):
            return int(func(*args, **kwargs))
        return wrapper

    def to_bool(self, func):
        def wrapper(*args, **kwargs):
            return bool(func(*args, **kwargs))
        return wrapper
td = TypeDecorators()
@td.to_int
def do_nothing(string: str):
    return string

@td.to_bool
def do_something(string: str):
    return string


if __name__ == '__main__':
    e = 'annbrr123@gmail.com'
    Validate.validate_email(e)
    e2 = 'annbrr123@gmail'
    Validate.validate_email(e2)

    w1 = Worker(1, 'Tanya', 'ASB', 'Vasya')
    w2 = Worker(2, 'Maryna', None, None)
    b2 = Boss(2, 'Ann', 'GRP')
    print(w2.my_boss)
    print(w1.my_boss)
    w2.my_boss = b2

    print(do_nothing('25'))
    print(do_something('True'))
