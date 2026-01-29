from typing import Any
from to_do import TODO


def task4(projects: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result = {}

    for project, details in projects.items():
         cost_value = details["costs"]
         for cost in cost_value:
             if cost == "None":
                cost.replace("None", -10)
             else:
                 cost *= 2
    return result

if __name__ == "__main__":

    print(task4({
    "Alpha" : {
    "project-id" : 11,
    "costs" : [1200.0, None, 950.0, None]},
    "Beta":{
    "project-id":22,
    "costs" : [None, 800.0, None, 700.0]},
    "Gamma":{
    "project-id" : 33,
    "costs" : [600.0, None, None, 500.0]
    }}))

