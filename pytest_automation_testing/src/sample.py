import pytest

@pytest.fixture
def sample_data():
    return {"name":"Alice", "age": 30}

@pytest.fixture
def temp_file():
    with open("temp.txt", "w") as f:
        f.write("test data")
    yield "temp.txt"
    import os
    os.remove("temp.txt")

