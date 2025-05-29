import pytest
from src.tasks.task2 import task2
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask2:
    test_cases = [
        # Example from description
        TestCase(
            given={
                "Phone": [4.0, 5.0, 4.5],
                "Tablet": [3.5, 4.0, 4.0],
                "Laptop": [5.0, 4.5, 4.5],
            },
            expected="Laptop",
        ),
        # Two products, clear winner
        TestCase(
            given={
                "A": [3.0, 3.0],
                "B": [5.0, 5.0],
            },
            expected="B",
        ),
        # Different number of ratings per product
        TestCase(
            given={
                "Product X": [4.0, 4.0, 4.0, 4.0],
                "Product Y": [5.0, 5.0],
                "Product Z": [3.0, 3.0, 3.0],
            },
            expected="Product Y",
        ),
        # Winner has only one rating
        TestCase(
            given={
                "Single": [5.0],
                "Multiple": [4.0, 4.0, 4.0],
            },
            expected="Single",
        ),
        # Larger dataset
        TestCase(
            given={
                "Low": [1.0, 2.0, 3.0],
                "Mid": [3.0, 3.5, 4.0],
                "High": [4.5, 4.5, 4.5],
            },
            expected="High",
        ),
        # Decimal averages
        TestCase(
            given={
                "Alpha": [4.2, 4.4],
                "Beta": [4.9, 4.8],
                "Gamma": [4.0, 4.1, 4.2],
            },
            expected="Beta",
        ),
        # Order should not matter
        TestCase(
            given={
                "Third": [2.0, 2.0],
                "First": [5.0, 5.0],
                "Second": [3.0, 3.0],
            },
            expected="First",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_grading(self, test_case: TestCase):
        ratings = test_case.given

        assert_equals(
            message=f"> ratings = {ratings}",
            expected=test_case.expected,
            actual=task2(ratings=ratings),
        )
