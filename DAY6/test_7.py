import pytest

@pytest.mark.skip
def test_funct():
	eno=450
	assert eno <500

def test_funct1():
	cname='abc'
	assert cname == 'abc'

def test_funct2():
	po=4590
	assert po >5000
