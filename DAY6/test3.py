import math
import pytest
#@pytest.mark.<MarkerName>

@pytest.mark.funct
def test_functblock1():
	n=25
	assert math.sqrt(n) == 5

@pytest.mark.funct
def test_functblock2():
	n=5
	assert 5+5 == 10

@pytest.mark.funct
def test_functblock3():
	n=15
	assert n <10