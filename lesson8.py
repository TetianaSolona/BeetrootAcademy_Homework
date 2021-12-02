if __name__ == '__main__':
    # Task 1
    # Create a simple function called favorite_movie,
    # which takes a string containing the name of your favorite movie.
    # The function should then print “My favorite movie is named {name}”.

    def favourite_movie():
        movie = input('What is your favourite movie?')
        print(f'My favourite movie is {movie}')
    favourite_movie()

    # Task 2
    # Create a function called make_country, which takes in a country’s name and capital as parameters.
    # Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter.
    # Make the function print out the values of the dictionary to make sure that it works as intended.

    def make_country(name, capital, **county_info):
        country = {}
        country['Name'] = name
        country['Capital'] = capital
        for key, value in county_info.items():
            country[key] = value
        return country
    info = make_country(name='Ukraine', capital='Kyiv')
    print(info)

    # task 3
    # Create a function called make_operation, which takes in a simple arithmetic
    # operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’)
    # and an arbitrary number of arguments (only numbers) as the second parameter.
    # Then return the sum or product of all the numbers in the arbitrary parameter.

    def make_operation(*num):
        sum = 0
        for i in num:
            sum += i
        print(f'Сума чисел равна: {sum}')

    make_operation(2, 3, 3)



