from typing import Any
from to_do import TODO


def task4(projects: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result = {}

    for project, details in projects.items():
         cost_value = details["costs"]
         for cost,value in cost_value.items():
             if value == "None"
                value.replace("None", -10)
    return result

if __name__ == "__main__":

    print(task4())
