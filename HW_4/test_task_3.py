import unittest

from task_3 import < 'ваша функция по созданию полиномов' > as target


# Класс с тестами
class TestClass(unittest.TestCase):

    def test_create_poly(self):
        """
        Метод тестирования функции создания полиномов.
        Функция должна принимать список коэффициентов полинома
        """

        args = [
            [0, 1, 2],
            [2, 0, 1],
            [1, 2, 0],
            [0, 0, 0],
        ]

        expects = [
            'x + 2 = 0',
            '2x^2 + 1 = 0',
            'x^2 + 2x = 0',
            '0 = 0',
        ]  # если ваша функция создает полиномы без пробелов, то удалите пребелы в results

        for arg, expect in zip(args, expects):
            self.assertEqual(target(arg), expect)


if __name__ == '__main__':
    unittest.main()
