"""
TASK: Given a string and a code word, print out an encoded string following the alphabet of the code word.
"""
import string


def encode(sent, code):
    """
    Encodes the given string following the position of the alphabets in the code word.

    :param sent: Given sentence to code
    :param code: The code word the encoding process follows
    :return: A single encoded string
    """
    alpha = string.ascii_uppercase
    new_sent = ''
    code_index = 0
    for j in sent:
        if j == " ":
            new_sent += " "
            continue

        alpha_shift = alpha.index(code[code_index % len(code)])
        alpha_add = alpha.index(j)
        enc = (alpha_shift + alpha_add) % 26
        new_sent += alpha[enc]
        code_index += 1

    return new_sent


#  Main Method
if __name__ == '__main__':
    n = int(input())
    answers = []
    for i in range(n):
        s = input()  # Sentence
        c = input()  # Code
        answers.append(encode(s, c))

    for i in answers:
        print(i)
