from math_series.series import (fibonacci, lucas, sum_series)

def test_fibonacci():
    actual = fibonacci(10)
    expected = 89
    assert actual == expected

   


def test_lucas():
    actual = lucas(9)
    expected = 76
    assert actual == expected


def test_math_new():
    actual = sum_series(5)
    expected = 8
    assert actual == expected


def test_math_fib():
    actual = sum_series(10,0,1)
    expected = 89
    assert actual == expected


def test_math_lucas():
    actual = sum_series(9,2,1)
    expected = 76
    assert actual == expected