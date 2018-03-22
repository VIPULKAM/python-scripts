from calc import add, sub, div, mul, check_input

class Test_Calc():

    def test_check_input(self):
        assert(check_input('10', '50') == (10, 50))

    def test_add(self):
        assert(add(5, 6) == 11)
        assert(add(-1, 1) == 0)
        assert(add(1.5, 9.5) == 11)
        assert(add(-1.5, -9.5) == -11)
        assert(add('10', '0') == 10)

    def test_sub(self):
        assert(sub(6, 5) == 1)
        assert(sub(-1, 1) == -2)
        assert(sub(1.5, 9.5) == -8.0)
        assert(sub(-1.5, -9.5) == 8.0)
        assert(sub('10', '0') == 10)


    def test_div(self):
        assert(div(6, 0) == None)
        assert(div(1, 1) == 1)
        assert(div(-16, 2) == -8)
        assert(div(-16, -2) == 8)
        assert(div(100, 25) == 4)
        assert(div('10', '2') == 5)

    def test_mul(self):
        assert(mul(6, 0) == 0)
        assert(mul(1, 1) == 1)
        assert(mul(-16, 2) == -32)
        assert(mul(-16, -2) == 32)
        assert(mul(100, 25) == 2500)
        assert(mul('10', '2') == 20)

