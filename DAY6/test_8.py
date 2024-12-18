import pytest

@pytest.mark.f1
def test_blk1():
	a=5
	b=6
	assert a+1 == b
@pytest.mark.f1
def test_blk2():
	a=10
	b=20
	assert a+10 == b