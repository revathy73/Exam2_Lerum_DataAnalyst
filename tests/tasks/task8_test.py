import pytest
from src.tasks.task8 import task8
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask8:
    test_cases = [
        # Example from description
        TestCase(
            given="a2b4c",  # (2 + 4) - 1 = 5
            expected=True,
        ),
        # Second example from description
        TestCase(
            given="abc3",  # (3) - 1 = 2
            expected=False,
        ),
        # Single digit divisible by 5 after subtraction
        TestCase(
            given="5",  # (5) - 1 = 4
            expected=False,
        ),
        # Single digit resulting in zero
        TestCase(
            given="1",  # (1) - 1 = 0
            expected=True,  # 0 is divisible by 5
        ),
        # Multiple digits
        TestCase(
            given="a1b2c3d4",  # (1+2+3+4) - 1 = 9
            expected=False,
        ),
        # Digits sum to 6
        TestCase(
            given="123",  # (1+2+3) - 1 = 5
            expected=True,
        ),
        # Digits sum to 11
        TestCase(
            given="a9b2",  # (9+2) - 1 = 10
            expected=True,
        ),
        # No digits
        TestCase(
            given="abc",  # (0) - 1 = -1
            expected=False,
        ),
        # Digits with symbols
        TestCase(
            given="!2@3#",  # (2+3) - 1 = 4
            expected=False,
        ),
        # Long mixed string
        TestCase(
            given="a1b2c3d4e5f6",  # (1+2+3+4+5+6) - 1 = 20
            expected=True,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_grading(self, test_case: TestCase):
        sentence = test_case.given

        assert_equals(
            message=f"> sentence = {sentence}",
            expected=test_case.expected,
            actual=task8(sentence=sentence),
        )
