# Recursion

# task 1
def to_power(x: int, exp: int):
    if exp == 1:
        return x
    return x * to_power(x, exp - 1)


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    l = len(looking_str)
    if l < 2:
        return True
    else:
        if looking_str[index] == looking_str[l-1]:
            return is_palindrome(looking_str[index+1:l-1])
        else:
            return False


# task 3
def mult(a: int, n: int) -> int:
    if a == 0 or n == 0:
        return 0
    if a > 0 and n > 0:
        return a + mult(a, n - 1)
    return 'Function works only with positive integers'


# task 4
def reverse(input_str: str) -> str:
    if len(input_str) == 0:
        return input_str
    else:
        return reverse(input_str[1:]) + input_str[0]


# task 5
def sum_of_digits(digit_string: str) -> int:
    try:
        digit_string_1 = int(digit_string)
        if digit_string_1 == 0:
            return 0
        return digit_string_1 % 10 + sum_of_digits(digit_string_1 / 10)
    except ValueError:
        return 'Function works only with digit'


if __name__ == '__main__':
    print(to_power(5, 5))
    print(is_palindrome('sassas'))
    print(mult(2, -3))
    print(reverse('python'))
    print(sum_of_digits('26'))
