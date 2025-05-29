from src.tasks import task10
from tests.helper.ClassSignature import ClassSignature
from tests.helper.custom_assertions import assert_class_signature, assert_equals
from tests.helper.FunctionSignature import FunctionSignature


class TestTask10:
    def test_initial_values_are_correct(self):
        self.__assert_class_signature()

        module = task10
        class_name = "Avatar"
        sut = getattr(module, class_name)()

        assert_equals(
            message="initial stamina",
            expected=8,
            actual=sut.stamina,
        )

        assert_equals(
            message="initial experience",
            expected=0,
            actual=sut.experience,
        )

    def test_train_decreases_stamina_by_one(self):
        self.__assert_class_signature()

        module = task10
        class_name = "Avatar"
        sut = getattr(module, class_name)()

        sut.train()

        assert_equals(
            message="stamina after one train",
            expected=7,
            actual=sut.stamina,
        )

    def test_rest_increases_stamina_by_one(self):
        self.__assert_class_signature()

        module = task10
        class_name = "Avatar"
        sut = getattr(module, class_name)()

        sut.rest()

        assert_equals(
            message="stamina after one rest",
            expected=9,
            actual=sut.stamina,
        )

    def test_evolve_increases_experience_by_one(self):
        self.__assert_class_signature()

        module = task10
        class_name = "Avatar"
        sut = getattr(module, class_name)()

        sut.evolve()

        assert_equals(
            message="experience after one evolve",
            expected=1,
            actual=sut.experience,
        )

    def test_multiple_train_calls_decrease_stamina_correctly(self):
        self.__assert_class_signature()

        module = task10
        class_name = "Avatar"
        sut = getattr(module, class_name)()

        sut.train()
        sut.train()
        sut.train()

        assert_equals(
            message="stamina after multiple train calls",
            expected=5,
            actual=sut.stamina,
        )

    def test_multiple_rest_calls_increase_stamina_correctly(self):
        self.__assert_class_signature()

        module = task10
        class_name = "Avatar"
        sut = getattr(module, class_name)()

        sut.rest()
        sut.rest()

        assert_equals(
            message="stamina after multiple rest calls",
            expected=10,
            actual=sut.stamina,
        )

    def test_multiple_evolve_calls_increase_experience_correctly(self):
        self.__assert_class_signature()

        module = task10
        class_name = "Avatar"
        sut = getattr(module, class_name)()

        sut.evolve()
        sut.evolve()
        sut.evolve()

        assert_equals(
            message="experience after multiple evolve calls",
            expected=3,
            actual=sut.experience,
        )

    def test_mixed_actions_update_stamina_and_experience_correctly(self):
        self.__assert_class_signature()

        module = task10
        class_name = "Avatar"
        sut = getattr(module, class_name)()

        sut.train()  # stamina 7
        sut.evolve()  # experience 1
        sut.rest()  # stamina 8
        sut.train()  # stamina 7
        sut.evolve()  # experience 2

        assert_equals(
            message="final stamina",
            expected=7,
            actual=sut.stamina,
        )

        assert_equals(
            message="final experience",
            expected=2,
            actual=sut.experience,
        )

    def __assert_class_signature(self):
        module = task10
        class_name = "Avatar"

        assert_class_signature(
            module=module,
            class_signature=ClassSignature(
                class_name=class_name,
                properties=[],
                methods=[
                    FunctionSignature(function_name="train", number_of_parameters=1),
                    FunctionSignature(function_name="rest", number_of_parameters=1),
                    FunctionSignature(function_name="evolve", number_of_parameters=1),
                ],
            ),
        )
