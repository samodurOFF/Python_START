import unittest

from task_1 import < 'Ваша функция' > as target  # Функция должна принимать выражение в виде строки


# Класс с тестами
class TestClass(unittest.TestCase):

    def test_simple_expression(self):
        """
        Тестирование простого выражения.
        """

        arg = '1 + 2'
        expect = 3
        self.assertEqual(target(arg), expect)

    def test_mult_div(self):
        """
        Тестирование приоритета умножения и деления
        """

        arg = '4 / 2 * 3'
        expect = 6
        self.assertEqual(target(arg), expect)

    def test_brackets(self):
        """
        Тестирование приоритета со скобками
        """

        arg = '(2 * (1 + 3) - 1) - (5 / 2)'
        expect = 4.5
        self.assertEqual(target(arg), expect)


if __name__ == '__main__':
    unittest.main()
