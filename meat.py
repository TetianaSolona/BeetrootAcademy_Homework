# Говядина — 666 грамм; Вино красное — 500мл; Оливковое масло — 100 мл;
# Сушеный чебрец — 2 ст.л.; Лавровый лист — 2 шт.; Петрушка сушеная — 1 ст.л.;
# Укроп сушеный — 1 ст.л.; Базилик сушеный — 1 ст.л.; Нитритная соль — 18 г. `
from functools import wraps

def meaning_rounder(dec=2):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            f = func(*args, **kwargs)
            return round(f, dec)
        return wrapper
    return decorator


def add_edz(edz):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            f = func(*args, **kwargs)
            return str(f) + ' ' + edz
        return wrapper
    return decorator

class Brezaola:
    def __init__(self, weight = 666):
        self.__weight = weight
        self.__coef = weight / 666

    def __round(self, val, dec=2):
        return round(val, dec)


    @property
    @meaning_rounder()
    def weight(self):
        return self.__weight

    @property
    @add_edz('мл')
    @meaning_rounder(0)
    def wine(self):
        return 500 * self.__coef

    @property
    @add_edz('мл')
    @meaning_rounder(0)
    def oil(self):
        return 100 * self.__coef

    @property
    @add_edz('ст.л')
    @meaning_rounder()
    def thyme(self):
        return 2 * self.__coef

    @property
    @add_edz('шт')
    @meaning_rounder()
    def leaf(self):
        return 2 * self.__coef

    @property
    @add_edz('ст.л')
    @meaning_rounder()
    def parsley(self):
        return 1 * self.__coef

    @property
    @add_edz('ст.л')
    @meaning_rounder()
    def dill(self):
        return 1 * self.__coef

    @property
    @add_edz('шт')
    @meaning_rounder()
    def basil(self):
        return 1 * self.__coef

    @property
    @add_edz('г')
    @meaning_rounder()
    def nintric_acid(self):
        return 18 * self.__coef

    def __str__(self):
        return f'''Рецепт Брезоола
Мясо:\t{self.weight}
Вино:\t{self.wine}
Оливковое масло:\t{self.oil}
Сушеный чебрец:\t{self.thyme}
Лавровый лист:\t{self.leaf}
Петрушка сушеная:\t{self.parsley}
Укроп сушеный:\t{self.dill}
Базилик сушеный:\t{self.basil}
Нитритная соль:\t{self.nintric_acid}
'''

r1 = Brezaola(2000)
print(r1)