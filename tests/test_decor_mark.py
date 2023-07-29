import pytest


@pytest.Mark.smoke
def test_mark_1():
    assert True


@pytest.Mark.regress
def test_mark_2():
    assert True

@pytest.Mark.regress
def test__mark_3():
    assert True

@pytest.Mark.regress
def test_mark_4():
    assert True