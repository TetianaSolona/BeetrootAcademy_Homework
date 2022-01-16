import unittest

#task 1

class Mathematician:

    def square_nums(self, *args):
        return [i**2 for i in args]

    def remove_positives(self, *args):
        return [i for i in args if i < 0]

    def filter_leaps(self, *args):
        return [i for i in args if i % 400 == 0 or i % 100 != 0 and i % 4 == 0]


class TestMathematic(unittest.TestCase):

    def setUp(self) -> None:
        self.num = Mathematician()

    def test_square(self):
        self.assertEqual(self.num.square_nums(3), [9], 'ops')
        self.assertEqual(self.num.square_nums(4, 5, 8), [16, 25, 64], 'ops')

    def test_remove(self):
        self.assertEqual(self.num.remove_positives(-9, 0, 1), [-9], 'ops')
        self.assertEqual(self.num.remove_positives(9, 0, 1), [], 'ops')
        self.assertEqual(self.num.remove_positives(-98, -7, -2), [-98, -7, -2], 'ops')

    def test_filter(self):
        self.assertEqual(self.num.filter_leaps(2020, 1986), [2020], 'ops')
        self.assertEqual(self.num.filter_leaps(2000, 1986), [2000], 'ops')

if __name__ == '__main__':
    unittest.main()