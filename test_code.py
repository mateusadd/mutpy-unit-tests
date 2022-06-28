from unittest import TestCase
from code import checkNumbersInputted

class Test(TestCase):
    def test_number1_greater_than_number2(self):
        self.assertEqual(checkNumbersInputted(2, 1), True)

    def test_number1_less_than_number2(self):
        self.assertEqual(checkNumbersInputted(1, 2), False)