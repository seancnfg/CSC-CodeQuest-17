up_keys = "qwertyuiop"
mid_keys = "asdfghjkl"
bot_keys = "zxcvbnm,."

capslock = False


def shift_line(line):
    """
    Shifts the given string to the left 1 keyboard key

    :param line: The given line we need to shift
    :return: A shifted string
    """
    global capslock
    lowered = line.lower()
    new_line = []
    for k in range(len(lowered)):
        new_char = ""
        if lowered[k] in up_keys:
            if lowered[k] == "q":
                new_char = "    "
            else:
                new_char = up_keys[up_keys.index(lowered[k]) - 1]
        elif lowered[k] in mid_keys:
            if lowered[k] == "a":
                capslock = not capslock
            else:
                new_char = mid_keys[mid_keys.index(lowered[k]) - 1]
        elif lowered[k] in bot_keys:
            if lowered[k] == "z":
                pass
            else:
                new_char = bot_keys[bot_keys.index(lowered[k]) - 1]
        else:
            new_char = " "

        # Testing to see if the given character is caps lock or uppercase
        if capslock:
            if not line[k].isalpha():
                new_char = new_char.upper()
            elif line[k].islower():
                new_char = new_char.upper()
            else:
                new_char = new_char.lower()
        else:
            if line[k].isupper():
                new_char = new_char.upper()

        new_line.append(new_char)

    return "".join(new_line)


if __name__ == '__main__':
    answers = []
    n = int(input())
    for _ in range(n):
        lines = int(input())
        for j in range(lines):
            s = input()
            answers.append(shift_line(s))

    for i in answers:
        print(i)
