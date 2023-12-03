"""This file contains functions that gets the csv and adds the nearest court data to this dict"""
import csv
from rich.progress import track

from requests import get

API_BASE_URL = "https://www.find-court-tribunal.service.gov.uk"


def get_people_csv() -> list[dict]:
    """Returns the data in the people csv file."""
    with open('people.csv', 'r', encoding='utf-8') as csv_file:
        return list(csv.DictReader(csv_file))


def get_nearest_court(postcode: str, court_type: str) -> list[dict]:
    """Gets and returns the necessary court data for a given postcode and court type."""

    response = get(
        f"{API_BASE_URL}/search/results.json?postcode={postcode}", timeout=10).json()

    if 'message' in response:
        raise ValueError(response['message'])

    for court in response:
        if court_type in court['types']:
            return {'court_name': court['name'],
                    'dx_number': court['dx_number'],
                    'distance': court['distance']}

    raise ValueError('No courts found with that type')


def add_nearest_courts(people: list[dict]) -> list[dict]:
    """Combines the nearest court data to the person data and returns it."""

    combined_data = []

    for person in track(people):

        postcode = person['home_postcode']
        court_type = person['looking_for_court_type']

        court_data = get_nearest_court(postcode, court_type)

        combined_data.append({**person, **court_data})

    return combined_data


def save_to_csv(data: list[dict], filename: str) -> None:
    """Saves the given data to a specified file name."""

    with open(f"{filename}.csv", 'w', newline='', encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())

        writer.writeheader()

        for row in data:
            writer.writerow(row)


if __name__ == "__main__":

    people_data = get_people_csv()

    people_with_court_data = add_nearest_courts(people_data)

    save_to_csv(people_with_court_data, "nearest_courts")
