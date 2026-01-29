from typing import Any
from to_do import TODO


def task4(projects: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result = {}

    for project, details in projects.items():
        id = details["id"]
        costs = details["costs"]

        new_costs = []

        for cost in costs:
            if cost is None:
                new_costs.append(-10.0)
            else:
                new_costs.append(cost * 2)

        result[project] = {"project-id": id, "costs": new_costs}

    return result



