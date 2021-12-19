if __name__ == '__main__':
    # task 1
    # Write a Python program to detect the number of local variables declared in a function.
    def det_number():
        x = 'Hello'
        y = 'world'
        z = '1'
        return
    print(det_number.__code__.co_nlocals)

    # task 2
    # Write a Python program to access a function inside a function
    # (Tips: use function, which returns another function)
    def test(a):
        def add(b):
            return a + b
        return add
    c = test(2)
    print(c(4))

    # task 3
    # Write a function called `choose_func` which takes a list of nums and 2 callback functions.
    # If all nums inside the list are positive, execute the first function on that list and return the result of it.
    # Otherwise, return the result of the second one

    def choose_func(nums: list, func1, func2):
        for n in nums:
            if n < 0:
                return func2(nums)
        return func1(nums)

    def square_nums(nums):
        return [num ** 2 for num in nums]

    def remove_negatives(nums):
        return [num for num in nums if num > 0]



    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    print(choose_func(nums1, square_nums, remove_negatives))
    print(choose_func(nums2, square_nums, remove_negatives))



