import pytest
from calT.calculators import calculator
@pytest.fixture(scope="module")
def myfixture(request):
    print("开始计算")
    cal = calculator()
    yield cal
    print("计算结束")




