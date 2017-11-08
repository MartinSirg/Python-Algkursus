"""Generate list of princesses."""
import base64


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
    list_of_words = line.split()
    if len(list_of_words) < 1:
        return ["ERROR"]
    name = list_of_words[0]
    status = []
    list_of_words.remove(name)
    for word in list_of_words:
        if word.isupper() is True:
            status.append(word)
    for word in status:
        list_of_words.remove(word)
    status = " ".join(status)
    location = []
    for i in range(len(list_of_words)):
        if list_of_words[i][0].isupper() is True:
            location.append(list_of_words[i])
    if len(location) > 0:
        location.remove(location[-1])
    for word in location:
        if word in list_of_words:
            list_of_words.remove(word)
    details = " ".join(list_of_words)
    location = " ".join(location)
    result = [name, status, location, details]
    return result


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


def write(read_file):
    """
    Write the sorted lines to the new file 'princesses_to_save.txt'.

    The last princess is NOT followed by a blank line.

    Format:
            Name
            Status
            Place
            Details
            <NEW LINE>
    Example:
            Kathi
            FIGHTS FOR LIFE
            Old Shack
            Sassy
    :param read_file: the file we read from
    :return: None
    """
    file = open("princesses_to_save.txt", "w")
    princesses = sort_by_status(filter_by_status(read(read_file)))
    for i, princess in enumerate(princesses):
        for int2 in range(len(princess)):
            if len(princesses) - 1 != i:
                file.write(princess[int2] + "\n")
            else:
                if int2 < 3:
                    file.write(princess[int2] + "\n")
                else:
                    file.write(princess[3])
        if len(princesses) - 1 != i:
            file.write("\n")

if __name__ == '__main__':
    write("file.txt")
