from to_do import TODO


def task8(sentence: str) -> bool:

    total = 0

    for character in sentence:
        if character.isdigit():
            total += int(character)

    total = total - 1

    if total % 5 == 0:
        result = True
    else:
        result = False

    return result

if __name__ == "__main__":
    print(task8(sentence ="a2b4c"))
