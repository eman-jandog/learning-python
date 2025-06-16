# test_sample.py

import pytest
from src.sample import sample_data, temp_file

def add(a, b):
    return a + b

@pytest.mark.parametrize(
    "a, b, sum",
    [(2,3,5),(-1,1,0),(0,0,0),(10,1,11)]
)
def test_add(a,b,sum):
    assert add(a, b) == sum

def test_strings():
    assert "hello".upper() == "HELLO"
    assert 42 != 43

def test_sample_data(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30

def test_temp_file(temp_file):
    with open(temp_file, "r") as f:
        assert f.read() == "test data"

@pytest.mark.skip(reason="Not implemented yet.")
def test_unfinished():
    pass

@pytest.mark.slow
def test_slow_func():
    assert True