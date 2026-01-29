from pygments.lexer import words

from to_do import TODO


def task3(text: str) -> dict[str, int]:

    words = ""
    for character in text:
        if character not in (',','.',':',';'):
            words += character

    result = {}
    no_of_word = 0
    new_text = words.lower().split(" ")
    for index,word in enumerate(new_text):
        if word[0] == word[-1]:
            no_of_word += 1
            if word[0] not in result:
               result[word[0]] = no_of_word

    return result


if __name__ == "__main__":
    print(task3(text = "Anna area idea omega echo apple"))
