
from student import student

def test_total():
    assert student(80, 90, 70) == 240

def test_average():
    assert student(50, 60, 70) == 80

def test_percentage():
    assert student(50, 60, 70) == 80