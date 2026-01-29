from to_do import TODO


def task6(membership: str) -> bool:

    if membership is None or (len(membership) > 9) or (len(membership) < 9):
        return False

    result = False

    year = membership[0:4]
    member_code = membership[-3:]

    if year > 2015 and len(member_code) == 3 and member_code.isnumeric():
        return True

    return result

if __name__ == "__main__":

    print(task6(membership = 2017-567))
