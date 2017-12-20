"""Bus times."""
import re


class Main:
    """Combines File and Input classes."""

    def __init__(self, file: str):
        """Declare file as an object variable."""
        self.file = file

    def get_departure_time(self):
        """Ask input and print next bus time."""
        time = Input(input("Enter departure time- "))
        time.check_errors()
        hours, minutes = time.get_data()
        file_object = File(self.file)
        file_object.import_times_to_list()
        result_hours, result_mins = file_object.get_next_time(hours, minutes)
        result_mins = "{:02d}".format(result_mins)
        print(f"Your bus will depart at {result_hours}:{result_mins}")


class Input:
    """Deals with given user input."""

    def __init__(self, user_input: str):
        """Construct user input object value."""
        self.user_input = user_input

    def check_errors(self):
        """Check if input is correct.

        correct input is HH:MM or H:MM
        Raise Exception if false input
        """
        pattern = re.compile(r"([\d]{1,2}):([\d]{2})")
        match = re.match(pattern, self.user_input)
        if match is None:
            raise Exception
        elif int(match.group(1)) > 24 or int(match.group(2)) > 59:
            raise Exception

    def get_data(self):
        """Return int data from string form."""
        pattern = re.compile(r"([\d]{1,2}):([\d]{2})")
        match = re.match(pattern, self.user_input)
        hours = int(match.group(1))
        if hours == 24:
            hours = 0
        minutes = int(match.group(2))
        return hours, minutes


class File:
    """Deals with given text file containing bus files."""

    def __init__(self, file: str):
        """Declare file and times object variables."""
        self.file = file
        self.times = []

    def import_times_to_list(self):
        """Import bus times(HH:MM) into list."""
        if len(self.times) > 0:
            self.times.clear()
        with open(self.file) as f:
            for line in f.readlines():
                info = line.split()
                for i in range(1, len(info)):
                    time = int(info[0]), int(info[i])
                    self.times.append(time)

    def get_next_time(self, hours, mins):
        """Look at given time and return next time from bus schedule."""
        if len(self.times) == 0 or not isinstance(self.times, list):
            raise Exception("List is empty or is not list")
        last_time = self.times[-1]                          # if given time is bigger than last time
        if hours >= last_time[0] and mins >= last_time[1]:  # return first time
            return self.times[0]
        for time in self.times:                             # loop through times
            if time[0] < hours:                             # skip times before user hour
                continue
            elif time[0] == hours and time[1] <= mins:      # skip times that are on user hour but before user min
                continue
            elif time[0] == hours and time[1] > mins:       # bus time in the same hour as specified hour
                return time[0], time[1]
            else:                                           # first next hour time
                return time[0], time[1]
        return self.times[0]


""" Äge for loop
--------------------------------------------------------------------------
    def get_departure_time(self, inputs):
        time = Input(inputs)   # Input(input("Enter departure time- "))
--------------------------------------------------------------------------
for int1 in range(25):
    for j in range(60):
        j = "{:02d}".format(j)
        print(f"Input {int1}:{j}", end=" == ")
        Main("bussiajad.txt").get_departure_time(f"{int1}:{j}")"""
