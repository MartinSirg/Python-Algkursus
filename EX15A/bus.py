"""Bus times."""
import re


class Main:
    """DOCstring."""
    def __init__(self, file: str):
        """DOCstring."""
        self.file = file

    def get_departure_time(self):
        """DOCstring."""
        time = Input(input("Enter departure time- "))
        time.check_errors()
        hours, minutes = time.get_data()
        file_object = File(self.file)
        file_object.import_times_to_list()
        result_hours, result_mins = file_object.get_next_time(hours, minutes)
        result_hours = "{:02d}".format(result_hours)
        result_mins = "{:02d}".format(result_mins)
        print(f"Your bus will depart at {result_hours}:{result_mins}")


class Input:
    """DOCstring."""
    def __init__(self, user_input: str):
        self.user_input = user_input

    def check_errors(self):
        """DOCstring."""
        pattern = re.compile(r"(\d{1,2}):(\d{2})")
        match = re.match(pattern, self.user_input)
        if match is None:
            raise Exception
        elif int(match.group(1)) > 23 or int(match.group(2)) > 59:
            raise Exception

    def get_data(self):
        """DOCstring."""
        pattern = re.compile(r"(\d{1,2}):(\d{2})")
        match = re.match(pattern, self.user_input)
        hours = match.group(1)
        if hours[0] == "0":
            hours = hours[1]
        minutes = match.group(2)
        return int(hours), int(minutes)


class File:
    """DOCstring."""
    def __init__(self, file: str):
        """DOCstring."""
        self.file = file
        self.times = []

    def import_times_to_list(self):
        """DOCstring."""
        if len(self.times) > 0:
            return 0
        with open("bussiajad.txt") as f:
            for line in f.readlines():
                info = line.split()
                for i in range(1, len(info)):
                    time = int(info[0]), int(info[i])
                    self.times.append(time)

    def get_next_time(self, hours, mins):
        """DOCstring."""
        last_time = self.times[-1]                          # if given time is bigger than last time
        if hours >= last_time[0] and mins >= last_time[1]:  # return first time
            return self.times[0]
        for time in self.times:
            if time[0] < hours:
                continue
            elif time[0] == hours and time[1] <= mins:
                continue
            elif time[0] == hours and time[1] > mins:
                return time[0], time[1]
            else:
                return time[0], time[1]
