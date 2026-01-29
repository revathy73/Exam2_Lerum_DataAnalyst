from to_do import TODO


def task2(ratings: dict[str, list[float]]) -> str:

    result = ""

    highest_avg_rating = -1.0
    for product,rating in ratings.items():
        total = 0.0
        for rate in rating:
            total += rate
        average_rating = total / len(rating)
        if average_rating > highest_avg_rating:
            highest_avg_rating = average_rating
            result = product
    return result

if __name__ == "__main__":

    #print(task2(ratings= {"Phone" : [4.0, 5.0, 4.5],"Tablet" : [3.5, 4.0, 4.0],"Laptop" : [5.0, 4.5, 4.5]}))

    print(task2(ratings= {'Single': [5.0], 'Multiple': [4.0, 4.0, 4.0]}))

