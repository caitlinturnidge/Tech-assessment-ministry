"""Unit tests for task 2"""
from unittest.mock import patch, MagicMock

import pytest


from test_2 import get_nearest_court, add_nearest_courts


@patch('test_2.get')
def test_get_court_valid_output(mock_get):
    """Testing the correct keys are in the output from the API, and correct types are returned"""

    mock_response = MagicMock()

    mock_response.json.return_value = [
        {'name': "hello", 'hey': 'value', 'dx_number': '123',
            'distance': 'test', 'types': 'testing'},
        {"types": "None"}]

    mock_get.return_value = mock_response

    assert get_nearest_court('Test', "testing") == {
        'court_name': "hello", 'dx_number': '123', 'distance': 'test'}


@patch('test_2.get')
def test_get_court_but_no_types(mock_get):
    """Testing an error is raised if there are no courts of a certain type"""

    mock_response = MagicMock()

    mock_response.json.return_value = [
        {'name': "hello", 'hey': 'value', 'dx_number': '123',
            'distance': 'test', 'types': 'testing'},
        {"types": "None"}]

    mock_get.return_value = mock_response

    with pytest.raises(ValueError):
        get_nearest_court('Test', "type")


@patch('test_2.get')
def test_get_court_invalid_postcode(mock_get):
    """Testing an error is raised when postcode is invalid"""

    mock_response = MagicMock()

    mock_response.json.return_value = {'message': 'invalid'}

    mock_get.return_value = mock_response

    with pytest.raises(ValueError):
        get_nearest_court('Test', "type")


@patch('test_2.get_nearest_court')
def test_add_nearest_court_success(mock_get_nearest_court):
    """Testing the updated dict contains the correct keys"""

    mock_get_nearest_court.return_value = {'add': 'adding'}

    people = [
        {'home_postcode': 'hello', 'looking_for_court_type': 'testing', 'hello': 'hey'}]

    assert add_nearest_courts(people) == [
        {'home_postcode': 'hello', 'looking_for_court_type': 'testing', 'hello': 'hey', 'add': 'adding'}]
