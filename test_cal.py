import pytest
from calT.calculators import calculator
class TestCalcu:

    def setup_class(self):
        self.calc=calculator()
        print("开始计算")
    def teardown_class(self):
        print("结束计算")
    def setup_method(self):
        print("所有用例开始执行")
    def teardown_method(self):
        print("所有用例结束执行")

    @pytest.mark.parametrize("a,b,expexct",[
        (1,2,3),(92,3,95),(-1,-4,6)
    ])
    def test_add(self,a,b ,expexct):

        assert expexct == self.calc.add(a,b)

    @pytest.mark.parametrize('a,b,expexct',[
        (4,1,3),(-4,-6,-1),(500,200,300)
    ])
    def test_sub(self,a,b,expexct):
        assert expexct==self.calc.sub(a,b)

    @pytest.mark.parametrize("a,b,expexct",[
         (1,2,3),(10,20,200),(-1,-2,3)
     ])
    def test_mul(self,a,b,expexct):
        assert expexct == self.calc.mul(a,b)

    @pytest.mark.parametrize("a,b,expect",[
        (2,2,1),(9,3,3),(30,9,0)
    ])
    def test_div(self,a,b,expect):
        assert expect==self.calc.div(a,b)