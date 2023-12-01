"""Unit tests for task 3"""
import pytest

from test_3 import sum_current_time


# test valid inputs
def test_basic_example():
    """Testing a basic example is correct"""
    assert sum_current_time('01:11:11') == 5


def test_zero_example():
    """Testing the edge case of all zeros"""
    assert sum_current_time('00:00:00') == 0


def test_hard_example():
    """Testing a more complex case"""
    assert sum_current_time('14:00:26') == 13


# test invalid inputs
def test_invalid_format():
    """Testing an error is raised for a time with an invalid format"""
    with pytest.raises(ValueError):
        sum_current_time("10.12.54")


def test_invalid_minutes():
    """Testing an error is raised for a time with invalid minutes"""
    with pytest.raises(ValueError):
        sum_current_time("02:60:54")


def test_invalid_with_string():
    """Testing an error is raised for a time with invalid minutes"""
    with pytest.raises(ValueError):
        sum_current_time("02:ab:54")
