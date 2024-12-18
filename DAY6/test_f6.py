import pytest

@pytest.mark.parametrize("n,result",[(1,10),(2,20),(3,30),(4,40)])
def test_multipleinput(n,result):
	assert 10*n == result

