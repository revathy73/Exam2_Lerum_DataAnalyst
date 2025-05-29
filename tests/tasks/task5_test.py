import pytest
from src.tasks.task5 import task5
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask5:
    test_cases = [
        #  None input
        TestCase(
            given=None,
            expected={
                "vowels": 0,
                "consonants": 0,
                "numbers": 0,
            },
        ),
        # Example from description
        TestCase(
            given="He110",
            expected={
                "vowels": 1,  # e
                "consonants": 1,  # H
                "numbers": 3,  # 1, 1, 0
            },
        ),
        # Only vowels
        TestCase(
            given="aeiouAEIOU",
            expected={
                "vowels": 10,
                "consonants": 0,
                "numbers": 0,
            },
        ),
        # Only consonants
        TestCase(
            given="bcdfgBCDFG",
            expected={
                "vowels": 0,
                "consonants": 10,
                "numbers": 0,
            },
        ),
        # Only numbers
        TestCase(
            given="0123456789",
            expected={
                "vowels": 0,
                "consonants": 0,
                "numbers": 10,
            },
        ),
        # Only symbols
        TestCase(
            given="!@#$%^&*()_+-=,.;: ",
            expected={
                "vowels": 0,
                "consonants": 0,
                "numbers": 0,
            },
        ),
        # Mixed letters and numbers
        TestCase(
            given="a1b2c3",
            expected={
                "vowels": 1,
                "consonants": 2,
                "numbers": 3,
            },
        ),
        # Mixed with symbols (ignored)
        TestCase(
            given="A!e@I#oU%1^2&3",
            expected={
                "vowels": 5,
                "consonants": 0,
                "numbers": 3,
            },
        ),
        # Sentence-like input
        TestCase(
            given="Hello World 2023",
            expected={
                "vowels": 3,  # e, o, o
                "consonants": 7,  # H l l W r l d
                "numbers": 4,  # 2 0 2 3
            },
        ),
        # Spaces only
        TestCase(
            given="     ",
            expected={
                "vowels": 0,
                "consonants": 0,
                "numbers": 0,
            },
        ),
        # Single character cases
        TestCase(
            given="A",
            expected={
                "vowels": 1,
                "consonants": 0,
                "numbers": 0,
            },
        ),
        TestCase(
            given="b",
            expected={
                "vowels": 0,
                "consonants": 1,
                "numbers": 0,
            },
        ),
        TestCase(
            given="7",
            expected={
                "vowels": 0,
                "consonants": 0,
                "numbers": 1,
            },
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_grading(self, test_case: TestCase):
        text = test_case.given

        assert_equals(
            message=f"> text = {text}",
            expected=test_case.expected,
            actual=task5(text=text),
        )
