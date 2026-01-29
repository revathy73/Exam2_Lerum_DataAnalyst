from to_do import TODO


def task8(sentence: str) -> bool:

    result = False
    total = 0.0
    value = 0.0
    #text = int(sentence)
    for letter in sentence:
        if letter.isdigit():
            total += int(letter)
            value = total - 1
            if value % 5 == 0:
                result = True
    return result

if __name__ == "__main__":
    print(task8(sentence ="a2b4c"))
