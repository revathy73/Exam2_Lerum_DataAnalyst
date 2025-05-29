class TestCase:
    __test__ = False

    def __init__(self, given, expected):
        self.given = given
        self.expected = expected


class TestCase2:
    __test__ = False

    def __init__(self, given1, given2, expected):
        self.given1 = given1
        self.given2 = given2
        self.expected = expected


class TestCase3:
    __test__ = False

    def __init__(self, given1, given2, given3, expected):
        self.given1 = given1
        self.given2 = given2
        self.given3 = given3
        self.expected = expected
