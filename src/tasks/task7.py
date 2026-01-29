import math
from typing import Any
from to_do import TODO
import math

def task7(items: list[dict[str, Any]]) -> str:

    if len(items) == 0:
        return ""

    lowest_price = math.inf
    result = ""

    for item in items:
        if item["price"] < lowest_price:
            lowest_price = item["price"]
            result = item["name"]

    return result

