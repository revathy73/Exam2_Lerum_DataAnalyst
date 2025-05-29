import pytest
from src.tasks.task4 import task4
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask4:
    test_cases = [
        # Example from description
        TestCase(
            given={
                "Alpha": {
                    "project-id": 11,
                    "costs": [1200.0, None, 950.0, None],
                },
                "Beta": {
                    "project-id": 22,
                    "costs": [None, 800.0, None, 700.0],
                },
                "Gamma": {
                    "project-id": 33,
                    "costs": [600.0, None, None, 500.0],
                },
            },
            expected={
                "Alpha": {
                    "project-id": 11,
                    "costs": [2400.0, -10.0, 1900.0, -10.0],
                },
                "Beta": {
                    "project-id": 22,
                    "costs": [-10.0, 1600.0, -10.0, 1400.0],
                },
                "Gamma": {
                    "project-id": 33,
                    "costs": [1200.0, -10.0, -10.0, 1000.0],
                },
            },
        ),
        # Single project, mixed values
        TestCase(
            given={
                "Solo": {
                    "project-id": 1,
                    "costs": [None, 100.0, None],
                },
            },
            expected={
                "Solo": {
                    "project-id": 1,
                    "costs": [-10.0, 200.0, -10.0],
                },
            },
        ),
        # No  None values
        TestCase(
            given={
                "Clean": {
                    "project-id": 2,
                    "costs": [50.0, 75.0],
                },
            },
            expected={
                "Clean": {
                    "project-id": 2,
                    "costs": [100.0, 150.0],
                },
            },
        ),
        # All values  None
        TestCase(
            given={
                "Broken": {
                    "project-id": 3,
                    "costs": [None, None],
                },
            },
            expected={
                "Broken": {
                    "project-id": 3,
                    "costs": [-10.0, -10.0],
                },
            },
        ),
        # Empty costs list
        TestCase(
            given={
                "Empty": {
                    "project-id": 4,
                    "costs": [],
                },
            },
            expected={
                "Empty": {
                    "project-id": 4,
                    "costs": [],
                },
            },
        ),
        # Multiple projects, varying list sizes
        TestCase(
            given={
                "A": {
                    "project-id": 10,
                    "costs": [10.0],
                },
                "B": {
                    "project-id": 20,
                    "costs": [None, 20.0],
                },
            },
            expected={
                "A": {
                    "project-id": 10,
                    "costs": [20.0],
                },
                "B": {
                    "project-id": 20,
                    "costs": [-10.0, 40.0],
                },
            },
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_grading(self, test_case: TestCase):
        projects = test_case.given

        assert_equals(
            message=f"> projects = {projects}",
            expected=test_case.expected,
            actual=task4(projects=projects),
        )
