"""Generate list of princesses."""
import base64
import re


class InvalidPrincessException(Exception):
    """Throw this error, when invalid operation with princess."""
    pass


def read(read_file) -> list:
    """
    Read, decrypt and save information from the given file.

    :param read_file: the file we read from
    :exception: Exception
    :return: lines
    """
    list_of_princesses = []
    try:
        with open(read_file) as file:
            for i, line in enumerate(file):
                if i < 3:
                    continue
                else:
                    decoded_line = decode(line)
                    info = extract_information(decoded_line)
                    if None in info[0:2]:
                        raise InvalidPrincessException("Invalid princess!")
                    list_of_princesses.append(info)
    except FileNotFoundError:
        raise FileNotFoundError("File not found!")
    return list_of_princesses


def decode(line: str) -> str:
    """
    Decode each line.

    Hint: base64.
    :param line: line from the encoded file.
    :return: same decoded line. String.
    """
    b = base64.b64decode(line)
    return b.decode()


def extract_information(line: str) -> list:
    """
    Extract information from each line (without spaces or extra tabulation symbols).

    Example output: ['Helen-elizabeth', 'IN PANIC', 'Ancient Ruins', None]
    Example output: ['Julianne', 'EATEN', 'Heaven', 'Will rule the kingdom'].
    Obviously, she won't rule anything, however. How sad.
    :param line: decrypted line from the file.
    :return: information about single princess
    """
    line = line.strip("\n")
    princess = re.split(r'[ ]{2,}', line)
    return princess


def filter_by_status(lines) -> list:
    """
    Filter out non-relevant statuses.

    Statuses to filter: "EATEN", "SAVED", "SLAYED THE DRAGON HERSELF". There is no point to save those.

    :param lines: lines
    :return: list
    """
    false_status = ["EATEN", "SAVED", "SLAYED THE DRAGON HERSELF"]
    princesses = []
    for princess in lines:
        if princess[1] not in false_status:
            princesses.append(princess)
    return princesses


def sort_by_status(filtered_lines) -> list:
    """
    Sort lines by pattern FIGHTS FOR LIFE > INJURED > IN PANIC > BORED.

    FIGHTS FOR LIFE comes before INJURED etc.

    :param filtered_lines:
    :return: sorted lines.
    """
    in_order = []
    order = ["FIGHTS FOR LIFE", "INJURED", "IN PANIC", "BORED"]
    for i in range(4):
        for princess in filtered_lines:
            if princess[1] == order[0]:
                in_order.append(princess)
        order.remove(order[0])
    return in_order


def sort_by_place(sorted_lines):
    """
    Sort another sorted_list in order the places appear in the first place.

    :param sorted_lines:
    :return: list of sorted princesses:
    """
    order = []
    princess_in_place = {
        "Dark Cave": [],
        "Dungeon": [],
        "Old Shack": [],
        "High Mountain": [],
        "Abandoned Prison": [],
        "Misty Swamp": [],
        "Ancient Ruins": [],
        "Castle": [],
        "Pub": [],
        "Town Hall": [],
        "Office": [],
    }
    false_status = ["EATEN", "SAVED", "SLAYED THE DRAGON HERSELF"]
    for princess in sorted_lines:
        place = princess[2]
        status = princess[1]
        if status is None:
            raise InvalidPrincessException("Invalid princess!")
        elif status in false_status:
            raise InvalidPrincessException("The princess is already {status}!")
        if place not in order:
            order.append(place)
            princess_in_place[place].append(princess)
        else:
            princess_in_place[place].append(princess)
    result = []
    for place in order:
        result += princess_in_place[place]
    return result


def write(read_file):
    """
    Write the sorted lines to the new file 'princesses_to_save.txt'.

    :param read_file: the file we read from
    :return: None
    """
    list_of_princesses = sort_by_place(sort_by_status(filter_by_status(read(read_file))))
    with open("princesses_to_save.txt", "w") as file:
        file.write("NAME" + " " * 26 + "STATUS" + " " * 24 + "LOCATION" + " " * 22 + "DETAILS" + "\n")
        file.write("=" * 120 + "\n")
        file.write("\n")
        for i, princess in enumerate(list_of_princesses):
            for int2, value in enumerate(princess):
                if int2 < 3:
                    file.write(value + " " * (30 - len(value)))
                else:
                    file.write(value)
            if i != len(list_of_princesses) - 1:
                file.write("\n")


if __name__ == '__main__':
    write("file.txt")
