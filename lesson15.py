if __name__ == '__main__':

    # task 1
    def logger(func):

        def wrapper(*args):
            print(f'Function "{func.__name__}" has arguments of function {args}')
            func(*args)
        return wrapper

    @logger
    def add(x, y):
        return x + y

    @logger
    def square_all(*args):
        return [arg ** 2 for arg in args]


    # task 2
    def remove(words):
        words = ['pepsi', 'BMW']
        def stop_words(func):
            def wrapper(*args, **kwargs):
                f = func(*args, **kwargs)
                if type(f) is str:
                    for word in words:
                        f = f.replace(word, '*')
                return f
            return wrapper
        return stop_words


    @remove(['pepsi', 'BMW'])
    def create_slogan(name: str) -> str:
        return f"{name} drinks pepsi in his brand new BMW!"

    print(create_slogan('Ann'))

    # task 3
    def arg_rules(type_: type, max_length: int, contains: list):
        max_length: 15
        type_: str
        contains: []
        def rules(func):
            def wrapper(name):
                f = func(name)
                if type(name) != type_ or len(name) > max_length:
                    return False
                for contain in contains:
                    if name.find(contain) == -1:
                    # if any(name in contain for contain in contains): нашла вариант с any, если так можно
                        return False
                return f
            return wrapper
        return rules

    @arg_rules(type_=str, max_length=15, contains=['05', '@'])
    def create_slogan(name: str) -> str:
        return f"{name} drinks pepsi in his brand new BMW!"


    print(create_slogan('johndoe05@gmail.com'))
    print(create_slogan('S@SH05'))