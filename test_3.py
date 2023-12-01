"""This file contains the working function, which returns the sum of all the digits in the time"""


def sum_current_time(time_str: str) -> int:
    """Returns the sum of the digits in the time given."""

    # Check time is in a valid string format
    if len(time_str) != 8 or ':' not in time_str:
        raise ValueError('Time is not in the correct format')

    # Check the time str has valid hours, minutes and seconds.
    times = time_str.split(':')
    for i, time in enumerate(times):
        try:
            times[i] = int(time)
        except Exception as e:
            raise ValueError('Time not valid') from e

    if times[0] > 24:
        raise ValueError('Hour cannot be larger than 24')

    if times[1] >= 60:
        raise ValueError('Minutes cannot be larger than 60')

    if times[2] >= 60:
        raise ValueError('Seconds cannot be larger than 60')

    # Sum the digits in the time
    time_str = time_str.replace(":", '')
    total = 0
    for digit in time_str:
        total += int(digit)

    return total
