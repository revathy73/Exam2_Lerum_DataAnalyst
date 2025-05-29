from tests.helper.FunctionSignature import FunctionSignature


class ClassSignature:
    def __init__(
        self, class_name: str, properties: list[str], methods: list[FunctionSignature]
    ):
        self.class_name = class_name
        self.properties = properties
        self.methods = methods
