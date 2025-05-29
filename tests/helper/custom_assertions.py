import re
from inspect import signature

from pytest import approx

from tests.helper.ClassSignature import ClassSignature
from tests.helper.FunctionSignature import FunctionSignature


def assert_pseudocode(actual: str):
    assert type(actual) is str, __message(
        given="Complete the Pseudocode",
        expected="Your pseudocode solution",
        actual="Your solution is missing",
    )


def assert_printed(message: str, expected: str, pattern: str, capfd):
    out, err = capfd.readouterr()
    assert re.match(pattern, out), __message(message, expected, out)


def assert_type(message: str, actual, expected):
    assert isinstance(actual, expected), __message(
        given=message, actual=type(actual), expected=expected
    )


def assert_equals(message: str, expected, actual):
    assert actual == expected, __message(message, expected, actual)


def assert_almost_equals(message: str, expected: float, actual: float):
    assert approx(actual, 0.01) == expected, __message(message, expected, actual)


def assert_function_signature(module, function_signature: FunctionSignature):
    __assert_function_exists(module, function_signature.function_name)
    __assert_function_parameters(
        module,
        function_signature.function_name,
        function_signature.number_of_parameters,
    )


def __assert_function_exists(module, function_name: str):
    assert hasattr(module, function_name), __short_message(
        given=f"The function '{function_name}' is missing"
    )


def __assert_function_parameters(
    module, function_name: str, expected_number_of_parameters: int
):
    """
    This function throws an exception in the case the function does not exist in the module.
    """
    function = getattr(module, function_name)
    function_signature = signature(function)
    function_parameters = function_signature.parameters
    actual_number_of_parameters = len(function_parameters)

    error_message = __short_message(
        given=f"The function '{function_name}' must have {expected_number_of_parameters} parameters but {actual_number_of_parameters} were given",
    )

    assert expected_number_of_parameters == actual_number_of_parameters, error_message


def assert_class_signature(module, class_signature: ClassSignature):
    assert_class_exists(module, class_signature.class_name)
    __assert_class_properties(
        module, class_signature.class_name, class_signature.properties
    )

    klass = getattr(module, class_signature.class_name)
    for method in class_signature.methods:
        assert_function_signature(klass, method)


def assert_class_exists(module, class_name: str):
    assert hasattr(module, class_name), __short_message(
        given=f"The class '{class_name}' is missing"
    )


def __assert_class_properties(module, class_name: str, expected_properties: list[str]):
    """
    This function throws an exception in the case the class does not exist in the module.
    """
    klass = getattr(module, class_name)
    klass_properties = list(signature(klass).parameters.keys())

    for expected_property in expected_properties:
        assert expected_property in klass_properties, __short_message(
            given=f"The property '{expected_property}' is missing in the class '{class_name}'"
        )

    assert len(klass_properties) == len(expected_properties), __short_message(
        given=f"The class '{class_name}' must have {len(expected_properties)} properties but had {len(klass_properties)} instead"
    )


def __message(given, expected, actual) -> str:
    return """
==========INCORRECT RESULT==========
----- Input -----  
{}

----- Your Result ----- 
{}

----- Expected Result -----  
{}

====================================
    """.format(
        given,
        actual,
        expected,
    )


def __short_message(given) -> str:
    return """
==========INCORRECT RESULT==========
----- Input -----  
{}

====================================
    """.format(given)
