import pytest
from example_class import Dog

@pytest.fixture
def dog():
    dog = Dog("Terrence", "Bulldog")

def test_dog_initialization(dog):
    assert dog.get_name() == "Terrence"
    assert dog._breed() == "Bulldog"
    assert dog._tricks() == []