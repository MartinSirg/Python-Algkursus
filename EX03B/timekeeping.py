"""Time converter."""


def convert(time_string, from_seconds_in_minute, to_seconds_in_minute):
    """"
    1) Makes sure that there aren't more seconds in time_string than there are in from_seconds_in minute
    2) seconds: converts time_string into seconds
    3) new_minutes: finds minutes in new time and formats to show double digits
    4) new_seconds: finds seconds in new time and formats to show double digits
    5) new_time_string: joins new_minutes and new_seconds together as strings
    """
    if int(time_string[-2:]) > from_seconds_in_minute:
        return None
    else:
        seconds = int(time_string[0:2]) * from_seconds_in_minute + int(time_string[-2:])
        new_minutes = "{:02d}".format(seconds // to_seconds_in_minute)
        new_seconds = "{:02d}".format(seconds % to_seconds_in_minute)
        new_time_string = str(new_minutes) + ":" + str(new_seconds)
        return new_time_string
