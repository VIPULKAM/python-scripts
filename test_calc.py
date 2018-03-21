from calc import add, sub, div, mul, check_input
from unittest import TestCase, main

class Test_Calc(TestCase):

    def test_check_input(self):
        self.assertEqual(check_input('10', '50'), (10, 50))

    def test_add(self):
        self.assertEqual(add(5, 6), 11)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(1.5, 9.5), 11)
        self.assertEqual(add(-1.5, -9.5), -11)
        self.assertEqual(add('10', '0'), 10)

    def test_sub(self):
        self.assertEqual(sub(6, 5), 1)
        self.assertEqual(sub(-1, 1),-2)
        self.assertEqual(sub(1.5, 9.5), -8.0)
        self.assertEqual(sub(-1.5, -9.5), 8.0)
        self.assertEqual(sub('10', '0'), 10)


    def test_div(self):
        self.assertEqual(div(6, 0), None)
        self.assertEqual(div(1, 1),1)
        self.assertEqual(div(-16, 2),-8)
        self.assertEqual(div(-16, -2),8)
        self.assertEqual(div(100, 25), 4)
        self.assertEqual(div('10', '2'), 5)

    def test_mul(self):
        self.assertEqual(mul(6, 0), 0)
        self.assertEqual(mul(1, 1),1)
        self.assertEqual(mul(-16, 2),-32)
        self.assertEqual(mul(-16, -2),32)
        self.assertEqual(mul(100, 25), 2500)
        self.assertEqual(mul('10', '2'), 20)

if __name__ == '__main__':
    main()
