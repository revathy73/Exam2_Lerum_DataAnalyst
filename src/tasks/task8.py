from to_do import TODO


def task8(sentence: str) -> bool:

    result = False
    total = 0.0
    for character in sentence:
        if character.isdigit():
            total += character



    return result

if __name__ == "__main__":
    print(task8(sentence ="a2b4c"))
