import pytest
from src.tasks.task1 import task1
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase


class TestTask1:
    test_cases = [
        # Example from description
        TestCase(
            given={
                "Clean Code": {
                    "pages": 464,
                    "genre": "programming",
                },
                "The Hobbit": {
                    "pages": 310,
                    "genre": "fantasy",
                },
                "Short Stories": {
                    "pages": 120,
                    "genre": "fiction",
                },
            },
            expected="Short Stories-fiction",
        ),
        # Single book only
        TestCase(
            given={
                "Book A": {
                    "pages": 200,
                    "genre": "drama",
                },
            },
            expected="Book A-drama",
        ),
        # Two books, second has fewer pages
        TestCase(
            given={
                "Big Book": {
                    "pages": 1000,
                    "genre": "history",
                },
                "Small Book": {
                    "pages": 150,
                    "genre": "novel",
                },
            },
            expected="Small Book-novel",
        ),
        # First book has the fewest pages
        TestCase(
            given={
                "Tiny": {
                    "pages": 50,
                    "genre": "poetry",
                },
                "Medium": {
                    "pages": 200,
                    "genre": "essay",
                },
                "Large": {
                    "pages": 800,
                    "genre": "reference",
                },
            },
            expected="Tiny-poetry",
        ),
        # Books with large page differences
        TestCase(
            given={
                "Encyclopedia": {
                    "pages": 1200,
                    "genre": "education",
                },
                "Pamphlet": {
                    "pages": 10,
                    "genre": "marketing",
                },
                "Novel": {
                    "pages": 350,
                    "genre": "fiction",
                },
            },
            expected="Pamphlet-marketing",
        ),
        # Non-alphabetical insertion order
        TestCase(
            given={
                "Book C": {
                    "pages": 300,
                    "genre": "c",
                },
                "Book A": {
                    "pages": 100,
                    "genre": "a",
                },
                "Book B": {
                    "pages": 200,
                    "genre": "b",
                },
            },
            expected="Book A-a",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_grading(self, test_case: TestCase):
        library = test_case.given

        assert_equals(
            message=f"> library = {library}",
            expected=test_case.expected,
            actual=task1(library=library),
        )
