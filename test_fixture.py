import pytest
import  yaml
from calT.calculators import calculator
def get_datas():
    with open("datas.yml") as f:
        datas=yaml.safe_load(f)
        add_data=datas["add"]
        mul_data = datas["mul"]
        sub_data = datas["sub"]
        div_data = datas["div"]
        myid_data = datas["myid"]
        return [add_data,mul_data,sub_data,div_data,myid_data]

class TestCalcu:
    def setup_class(self):
        self.cal = calculator()
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect',get_datas()[0],ids=get_datas()[4])
    def test_add(self,a,b,expect):
        assert expect==self.cal.add(a,b)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect',get_datas()[2],ids=get_datas()[4])
    def test_sub(self, a, b, expect):
        assert expect == self.cal.sub(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas()[1], ids=get_datas()[4])
    def test_mul(self, a, b, expect,myfixture):
        assert expect == self.cal.mul(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect',get_datas()[3],ids=get_datas()[4])
    def test_div(self, a, b, expect):
        assert expect == self.cal.div(a, b)


