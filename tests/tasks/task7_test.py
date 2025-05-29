import pytest
from src.tasks.task7 import task7
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask7:
    test_cases = [
        # Empty list
        TestCase(
            given=[],
            expected="",
        ),
        # Single product
        TestCase(
            given=[
                {
                    "name": "Apple",
                    "quantity": 4,
                    "price": 0.75,
                },
            ],
            expected="Apple",
        ),
        # Two products (example case)
        TestCase(
            given=[
                {
                    "name": "Apple",
                    "quantity": 4,
                    "price": 0.75,
                },
                {
                    "name": "Bread",
                    "quantity": 2,
                    "price": 2.50,
                },
            ],
            expected="Apple",
        ),
        # Cheapest product appears last
        TestCase(
            given=[
                {"name": "Milk", "quantity": 1, "price": 1.20},
                {"name": "Cheese", "quantity": 1, "price": 3.50},
                {"name": "Water", "quantity": 1, "price": 0.50},
            ],
            expected="Water",
        ),
        # Cheapest product appears first
        TestCase(
            given=[
                {"name": "Banana", "quantity": 6, "price": 0.30},
                {"name": "Orange", "quantity": 4, "price": 0.80},
                {"name": "Grapes", "quantity": 1, "price": 2.00},
            ],
            expected="Banana",
        ),
        # Prices with decimals
        TestCase(
            given=[
                {"name": "ItemA", "quantity": 1, "price": 1.99},
                {"name": "ItemB", "quantity": 1, "price": 1.98},
                {"name": "ItemC", "quantity": 1, "price": 1.97},
            ],
            expected="ItemC",
        ),
        # Quantity should be ignored
        TestCase(
            given=[
                {"name": "BulkRice", "quantity": 100, "price": 10.0},
                {"name": "SingleCandy", "quantity": 1, "price": 1.0},
            ],
            expected="SingleCandy",
        ),
        # Equal prices — first encountered cheapest should be returned
        TestCase(
            given=[
                {"name": "A", "quantity": 1, "price": 2.0},
                {"name": "B", "quantity": 1, "price": 2.0},
            ],
            expected="A",
        ),
        # Many products
        TestCase(
            given=[
                {"name": "P1", "quantity": 1, "price": 5.0},
                {"name": "P2", "quantity": 1, "price": 4.0},
                {"name": "P3", "quantity": 1, "price": 3.0},
                {"name": "P4", "quantity": 1, "price": 2.0},
                {"name": "P5", "quantity": 1, "price": 1.0},
            ],
            expected="P5",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_grading(self, test_case: TestCase):
        items = test_case.given

        assert_equals(
            message=f"> items = {items}",
            expected=test_case.expected,
            actual=task7(items=items),
        )
