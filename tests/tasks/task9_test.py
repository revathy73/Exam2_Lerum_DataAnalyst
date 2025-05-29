import pytest
from src.tasks.task9 import task9
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask9:
    test_cases = [
        # Example #1 from description (no multiplier)
        TestCase(
            given="StarterXb",
            expected=37,
        ),
        # Example #2 from description (with multiplier)
        TestCase(
            given="StarterXb4",
            expected=148,
        ),
        # Only listed lowercase letters
        TestCase(
            given="aerst",
            expected=1 + 2 + 3 + 6 + 5,  # 17
        ),
        # Only listed uppercase letters
        TestCase(
            given="AERST",
            expected=1 + 2 + 3 + 6 + 5,  # 17
        ),
        # Lowercase letters not listed
        TestCase(
            given="bcdf",
            expected=4 * 4,  # 16
        ),
        # Uppercase letters not listed
        TestCase(
            given="BCDF",
            expected=8 * 4,  # 32
        ),
        # Mixed listed and non-listed, mixed case
        TestCase(
            given="SaRz",
            expected=6  # S
            + 1  # a
            + 3  # R
            + 4,  # z (lowercase, not listed)
        ),
        # Mixed letters with internal digits (no multiplier)
        TestCase(
            given="a2B3c",
            expected=1  # a
            + 8  # B
            + 4,  # c
        ),
        # Multiplier is zero
        TestCase(
            given="abc0",
            expected=0,  # (1 + 4 + 4) * 0
        ),
        # Multiplier is one
        TestCase(
            given="abc1",
            expected=9,  # (1 + 4 + 4) * 1
        ),
        # Long mixed input with multiplier
        TestCase(
            given="aErTsXyZ9",
            expected=(
                1  # a
                + 2  # E
                + 3  # r
                + 5  # T
                + 6  # s
                + 8  # X
                + 4  # y
                + 8  # Z
            )
            * 9,  # multiplier
        ),
        # Non-letter, non-digit characters ignored
        TestCase(
            given="a!e@r#t$",
            expected=1 + 2 + 3 + 5,
        ),
        # Last digit only determines multiplier
        TestCase(
            given="a2b3c4",
            expected=(1 + 4 + 4) * 4,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_grading(self, test_case: TestCase):
        sentence = test_case.given

        assert_equals(
            message=f"> sentence = {sentence}",
            expected=test_case.expected,
            actual=task9(sentence=sentence),
        )
