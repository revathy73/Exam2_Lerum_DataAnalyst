import pytest
from src.tasks.task3 import task3
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask3:
    test_cases = [
        # Example from description
        TestCase(
            given="Anna area idea omega echo apple",
            expected={
                "a": 2,
            },
        ),
        # Single matching word
        TestCase(
            given="Ada",
            expected={
                "a": 1,
            },
        ),
        # Multiple vowels matching
        TestCase(
            given="Anna Eve Otto",
            expected={
                "a": 1,
                "e": 1,
                "o": 1,
            },
        ),
        # Mixed case input
        TestCase(
            given="Anna AREA Ada",
            expected={
                "a": 3,
            },
        ),
        # Words start and end same letter but not vowels
        TestCase(
            given="Bob dad level",
            expected=dict(),
        ),
        # Punctuation should be ignored
        TestCase(
            given="Anna area Ada",
            expected={
                "a": 3,
            },
        ),
        # Words start with vowel but end differently
        TestCase(
            given="apple idea omega echo",
            expected=dict(),
        ),
        # Repeated words
        TestCase(
            given="Anna Anna Anna",
            expected={
                "a": 3,
            },
        ),
        # All vowels but only some match
        TestCase(
            given="area eve idea Otto",
            expected={
                "a": 1,
                "e": 1,
                "o": 1,
            },
        ),
        # Long sentence
        TestCase(
            given="Anna went to an area near an arena",
            expected={
                "a": 3,
            },
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_grading(self, test_case: TestCase):
        text = test_case.given

        assert_equals(
            message=f"> text = {text}",
            expected=test_case.expected,
            actual=task3(text=text),
        )
