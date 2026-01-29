from pygments.lexer import words

from to_do import TODO


def task3(text: str) -> dict[str, int]:

    result = {}

    new_text = text.lower().split(" ")
    for word in new_text:
        first = word [0]
        last = word [-1]
        if first == last:

            if first in ("a","e","i","o","u"):
                if first in result:
                    result[first] += 1
                else:
                    result[first] = 1

    return result


if __name__ == "__main__":
    print(task3(text = "Anna area idea omega echo apple"))
