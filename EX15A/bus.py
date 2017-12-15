"""Bus times."""
import re

class Main:
    def __init__(self, file: str):
        self.file = file

    def get_departure_time(self):
        time = Input(input("Enter departure time- "))
        time.check_errors()
        hours, minutes = time.get_data()
        print(hours, minutes)

class Input:
    def __init__(self, user_input : str):
        self.user_input = user_input

    def check_errors(self):
        pattern = re.compile(r"(\d{1,2}):(\d{2})")
        if re.match(pattern, self.user_input) is None:
            raise Exception("Valid time format is hh:mm or h:mm")

    def get_data(self):
        pattern = re.compile(r"(\d{1,2}):(\d{2})")
        match = re.match(pattern, self.user_input)
        hours = match.group(1)
        if hours[0] == "0":
            hours = hours[1]
        minutes = match.group(2)
        return int(hours), int(minutes)

class File:
    def __init__(self, file: str):
        self.file = file

    def read_file(self):
        ajad = []
        with open("bussiajad.txt") as f:
            for line in f.readlines():
                info = line.split()
                for i in range(1,len(info)):
                    time = info[0], info[i]
                    ajad.append(time)
        print(ajad)
    # TODO: ajad muutujas on ajad tuple vormides (hh:mm)

fail = File("bussiajad.txt")
fail.read_file()