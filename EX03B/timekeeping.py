"""Time converter."""


def convert(time_string, from_seconds_in_minute, to_seconds_in_minute):
    """
    Convert time from one time format to another.

    If there are more seconds in time_string than there are from_seconds_in_minute return None
    Convert time_string into seconds as an int
    Convert seconds back to minutes and seconds in the new time format.

    :param time_string: time format that will be converted
    :param from_seconds_in_minute: amount of seconds in a minute in the original time format
    :param to_seconds_in_minute: amount of seconds in a minute in the new time format
    :return: the new time format as a string
    """
    if int(time_string[-2:]) >= from_seconds_in_minute:
        return None
    else:
        seconds = int(time_string[0:2]) * from_seconds_in_minute + int(time_string[-2:])
        new_minutes = "{:02d}".format(seconds // to_seconds_in_minute)
        new_seconds = "{:02d}".format(seconds % to_seconds_in_minute)
        new_time_string = str(new_minutes) + ":" + str(new_seconds)
        return new_time_string
