'''
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
Чем больше тестов на каждую функцию - тем лучше
'''

from python import func_filter, func_map, func_sorted
import sys
from io import StringIO


def test_func_filter():
    assert func_filter(None, ['bool', 0, None, True, False, 1, 1-1, 2%2]) == ['bool', True, 1]
    assert func_filter(None, ['bool', 0]) == ['bool']
    assert func_filter(None, [None, True, False, 1]) == [True, 1]


def test_func_map(monkeypatch, capsys):
    assert func_map('1 5 4 5') == [1, 5, 4, 5]
    assert func_map('7 8 1 1 2') == [7, 8, 1, 1, 2]
    assert func_map('878 4554 5454') == [878, 4554, 5454]


def test_func_sorted():
    assert func_sorted([-878, 7878, -1, 0, 2454, 78]) == [7878, 2454, 78, 0, -1, -878]
    assert func_sorted([7, 8, 1, 1, 2]) == [8, 7, 2, 1, 1]
    assert func_sorted([878, 4554, 5454]) == [5454, 4554, 878]

