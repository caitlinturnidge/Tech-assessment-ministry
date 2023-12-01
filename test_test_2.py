"""Unit tests for task 2"""
import pytest
from unittest.mock import patch, MagicMock


from test_2 import get_nearest_court_data, add_nearest_court_data


@patch('test_2.get')
def test_get_court_valid_output(mock_get):
    """Testing the correct keys are in the output from the API, and correct types are returned"""

    mock_response = MagicMock()

    mock_response.json.return_value = [
        {'name': "hello", 'hey': 'value', 'dx_number': '123',
            'distance': 'test', 'types': 'testing'},
        {"types": "None"}]

    mock_get.return_value = mock_response

    assert get_nearest_court_data('Test', "testing") == {
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
        get_nearest_court_data('Test', "type")


@patch('test_2.get')
def test_get_court_invalid_postcode(mock_get):
    """Testing an error is raised when postcode is invalid"""

    mock_response = MagicMock()

    mock_response.json.return_value = {'message': 'invalid'}

    mock_get.return_value = mock_response

    with pytest.raises(ValueError):
        get_nearest_court_data('Test', "type")


@patch('test_2.get_people_csv')
@patch('test_2.get_nearest_court_data')
def test_add_nearest_court_success(mock_get_nearest_court_data, mock_get_people_csv):
    """Testing the updated dict contains the correct keys"""

    mock_get_people_csv.return_value = [
        {'home_postcode': 'hello', 'looking_for_court_type': 'testing', 'hello': 'hey'}]
    mock_get_nearest_court_data.return_value = {'add': 'adding'}

    final_dict = add_nearest_court_data()

    assert final_dict == [
        {'home_postcode': 'hello', 'looking_for_court_type': 'testing', 'hello': 'hey', 'add': 'adding'}]
