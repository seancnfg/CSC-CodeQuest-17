"""
TASK: Given n number of strings, print each string so that each word is reversed,
preserving capitalization and punctuation.
"""


def rev_string(s):
    """
    Takes the given string argument and calls 'rev_word' function to reverse each word.

    :param s: given string sentence to reverse
    :return: a sentence with each word reversed of type 'str', preserving capitalization and punctuation
    """
    sent = s.split()
    new_sent = []
    for j in sent:
        new_sent.append(rev_word(j))

    return " ".join(new_sent)


def rev_word(word):
    """
    Takes the given word argument and reverses it, preserving capitalization and punctuation.

    :param word: given word to reverse
    :return: the reversed word of type 'str'
    """
    # TODO: Implement punctuation
    # Let's take the word "Sal.ly!"

    new_word = []
    # Filter out the punctuation. We will deal with capitalization.
    alpha = list(filter((lambda x: x.isalpha()), word))  # ['S', 'a', 'l', 'l', 'y']
    backwards = list(reversed(list(map(lambda x: x.lower(), alpha))))  # ['y', 'l', 'l', 'a', 's']

    for j in range(0, len(backwards)):
        if alpha[j].isupper():
            new_word.append(backwards[j].upper())
        else:
            new_word.append(backwards[j])  # We already made it lowercase, so we don't need to use .lower() again.

    # Now, the punctuation.
    for j in range(0, len(word)):  # Iterate through original word
        if not word[j].isalpha():  # If the letter is not an alphabet
            new_word.insert(j, word[j])  # Insert the character at new word's index 'j'

    return "".join(new_word)


# Main method
if __name__ == "__main__":
    n = int(input())
    strings = []
    for i in range(0, n):
        strings.append(input())

    for i in strings:
        print(rev_string(i))
