import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_INT_WITHOUT_COLON


class TestExercise1203(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1203"

    def run_exercise(self, *inputs: int) -> list[str]:
        """Runs the exercise with the given inputs and captures the output."""
        with patch("builtins.input", side_effect=list(inputs)):
            with patch("sys.stdout", new = io.StringIO()) as fake_out:
                if self.MODULE_NAME in sys.modules:
                    importlib.reload(sys.modules[self.MODULE_NAME])
                else:
                    importlib.import_module(self.MODULE_NAME)

        output = fake_out.getvalue()
        return output.strip().splitlines()

    def validateRegex(self, line: str) -> None:
        self.assertRegex(line, REGEX_FOR_LETTERS, "The print must contain a sentence explaining the result.")

    def test_greater_than(self):
        lines = self.run_exercise(11, 10)
        greater = lines[0].lower().__contains__("mayor")
        m = re.findall(REGEX_FOR_INT_WITHOUT_COLON, lines[0])
        self.assertIsNotNone(m)
        self.assertTrue(m.__contains__("11"))
        self.assertTrue(m.__contains__("10"))
        self.assertTrue(greater)
        self.validateRegex(lines[0])

    def test_less_than(self):
        lines = self.run_exercise(9, 10)
        less = lines[0].lower().__contains__("menor")
        m = re.findall(REGEX_FOR_INT_WITHOUT_COLON, lines[0])
        self.assertIsNotNone(m)
        self.assertTrue(m.__contains__("9"))
        self.assertTrue(m.__contains__("10"))
        self.assertTrue(less)
        self.validateRegex(lines[0])

    def test_equal(self):
        lines = self.run_exercise(10, 10)
        equal = lines[0].lower().__contains__("igual")
        m = re.findall(REGEX_FOR_INT_WITHOUT_COLON, lines[0])
        self.assertIsNotNone(m)
        self.assertTrue(m.__contains__("10"))
        self.assertTrue(m.__contains__("10"))
        self.assertTrue(equal)
        self.validateRegex(lines[0])


if __name__ == '__main__':
    unittest.main()
