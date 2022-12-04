import unittest

from task_4 import < 'Ваша функция по сложению полиномов' > as target


# Класс с тестами
class TestClass(unittest.TestCase):

    def test_sum_poly(self):
        """
        Метод тестирования функции сложения полиномов.
        Аргументами функции должны быть строки в виде полиномов.
        """

        # Если ваши полиномы не имеют пробелов, то уберите их в строках ниже.
        poly_1 = '5x^5 + 15x^3 + 7x + 1 = 0'
        poly_2 = '10x^5 + 2x^4 + 11x^3 + 9x^2 + 3x = 0'

        expect = '15x^5 + 2x^4 + 26x^3 + 9x^2 + 10x + 1 = 0'
        self.assertEqual(target(poly_1, poly_2), expect)


if __name__ == '__main__':
    unittest.main()
