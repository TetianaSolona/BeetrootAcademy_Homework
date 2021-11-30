if __name__ == '__main__':

    # task 1
    # Make a program that has some sentence (a string) on input and
    # returns a dict containing all unique words as keys and the number of occurrences as values.

    def word_count(str):
        count = dict()
        words = str.split()

        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
        return count
    print(word_count('he has a cat and a dog at hom'))

    sentence = 'he has a cat and a dog at hom'

    # task 2
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    def dict_mul(d1, d2):
        d3 = dict()
        for k in d1:
            if k in d2:
                d3[k] = d1[k] * d2[k]
        return d3
    print(dict_mul(stock, prices))
    print(sum(dict_mul(stock, prices).values()))

    # task 3
    # Use a list comprehension to make a list containing tuples (i, j)
    # where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.
    a = [(i, i ** 2) for i in range(0, 10)]
    print(a)