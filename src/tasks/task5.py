from to_do import TODO


def task5(text: str) -> dict[str, int]:

    result = {"vowels" : 0,"consonants" : 0, "numbers" : 0}

    vowels = 'a','e','i','o','u'

    for letter in text:
        if letter.lower() in vowels and letter not in result:
            result["vowels"] = result["vowels"] + 1
        elif letter.lower().isalpha() and letter not in vowels and letter not in result:
            result["consonants"] = result["consonants"] + 1
        elif letter.isdigit():
            result["numbers"] = result["numbers"] + 1

    return result

if __name__ == "__main__":

    print(task5(text= "He110"))