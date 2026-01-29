from typing import Any
from to_do import TODO
import math


def task1(library: dict[str, dict[str, Any]]) -> str:
    result = ""
    least_number = math.inf

    for book_name,details in library.items():
        no_of_pages = details["pages"]
        book_special = details["genre"]
        if no_of_pages < least_number:
            least_number = no_of_pages
            #genre = book_special
            result = print(f"{book_name}-{book_special}")

    return result

if __name__ == "__main__":

    print(task1(library= {
    "Clean Code" : {
        "pages" : 464,
        "genre" : "programming"
    },
    "The Hobbit" : {
        "pages" : 310,
        "genre" : "fantasy"
    },
    "Short Stories" : {
        "pages" : 120,
        "genre" : "fiction"
    }
    }))
