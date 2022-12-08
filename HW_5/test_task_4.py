import unittest

from task_4 import < 'Ваша функция по RLE шифрованию' > as encode
from task_4 import < 'Ваша функция по по восстановлению зашифрованной строки' > as decode


# Класс с тестами
class TestClass(unittest.TestCase):
    arg = 'ffffffffffff11111111111      aaaaa'
    expect = '9f3f91216 5a'

    def test_rle_encode(self):
        """
        Метод тестирования функции RLE шифрования.
        Функция принимает строку.
        """

        self.assertEqual(encode(self.arg), self.expect)

    def test_rle_decode(self):
        """
        Метод тестирования функции восстановления строки, зашифрованной по RLE алгоритму.
        Функции принимает шифрованную строку.
        """

        self.arg, self.expect = self.expect, self.arg
        self.assertEqual(decode(self.arg), self.expect)


if __name__ == '__main__':
    unittest.main()
