"""This file contains functions that gets the csv and adds the nearest court data to this dict"""
import csv
import json
from rich.progress import track

from requests import get


def get_nearest_court_data(postcode: str, court_type: str) -> list[dict]:
    """Gets and returns the necessary data for a given postcode"""

    response = get(
        f"https://www.find-court-tribunal.service.gov.uk/search/results.json?postcode={postcode}",
        timeout=10)

    response = response.json()

    if 'message' in response:
        raise ValueError('Invalid Postcode')

    data = {}

    for court in response:
        if court_type in court['types']:
            data['court_name'] = court['name']
            data['dx_number'] = court['dx_number']
            data['distance'] = court['distance']
            return data

    raise ValueError('No courts found with that type')


def get_people_csv() -> list[dict]:
    """Returns the data in the people csv file"""
    with open('people.csv', 'r', encoding='utf-8') as csv_file:
        return list(csv.DictReader(csv_file))


def add_nearest_court_data() -> list[dict]:
    """Adds the nearest court data to the current people data dicts"""

    updated_people_data = []

    people = get_people_csv()
    for person in track(people):
        court_data = get_nearest_court_data(
            person['home_postcode'], person['looking_for_court_type'])
        person.update(court_data)
        updated_people_data.append(person)

    return updated_people_data


if __name__ == "__main__":
    all_data = add_nearest_court_data()
    print(json.dumps(all_data, indent=4))

    # Could add the data to a new csv as well
