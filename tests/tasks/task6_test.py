import pytest
from src.tasks.task6 import task6
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask6:
    test_cases = [
        #  None input
        TestCase(
            given=None,
            expected=False,
        ),
        # Valid minimum year
        TestCase(
            given="2015-000",
            expected=True,
        ),
        # Valid recent year
        TestCase(
            given="2023-123",
            expected=True,
        ),
        # Valid format, different member codes
        TestCase(
            given="2018-999",
            expected=True,
        ),
        # Year before 2015 (invalid)
        TestCase(
            given="2014-123",
            expected=False,
        ),
        TestCase(
            given="2010-999",
            expected=False,
        ),
        # Invalid formatting (missing dash)
        TestCase(
            given="2015123",
            expected=False,
        ),
        TestCase(
            given="2015+123",
            expected=False,
        ),
        # Invalid year length
        TestCase(
            given="201-123",
            expected=False,
        ),
        TestCase(
            given="20155-123",
            expected=False,
        ),
        # Invalid member code length
        TestCase(
            given="2015-12",
            expected=False,
        ),
        TestCase(
            given="2015-1234",
            expected=False,
        ),
        # Non-numeric year
        TestCase(
            given="ABCD-123",
            expected=False,
        ),
        # Non-numeric member code
        TestCase(
            given="2015-ABC",
            expected=False,
        ),
        TestCase(
            given="2016-1A3",
            expected=False,
        ),
        # Extra characters
        TestCase(
            given="2015-123-extra",
            expected=False,
        ),
        # Leading/trailing spaces should invalidate
        TestCase(
            given=" 2015-123 ",
            expected=False,
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_grading(self, test_case: TestCase):
        membership = test_case.given

        assert_equals(
            message=f"> membership = {membership}",
            expected=test_case.expected,
            actual=task6(membership=membership),
        )
