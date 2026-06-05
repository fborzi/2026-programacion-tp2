import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_INT_ONLY, REGEX_FOR_STRING_WITHOUT_COLON


class TestExercise1210(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1210"

    def run_exercise(self, *inputs: float) -> list[str]:
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

    def test_revenues(self):
        lines = self.run_exercise(100, -20, 250, 3, 0)

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])
        m2 = re.findall(REGEX_FOR_INT_ONLY, lines[1])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertIsNotNone(m2)
        self.assertTrue(m1[0].lower().__contains__("negativo"))
        self.assertTrue(m2[0].__contains__("353"))
        self.validateRegex(lines[1])

    def test_missing_input(self):
        with self.assertRaises(StopIteration):
            self.run_exercise(5, 1, 2, 3, 4)


if __name__ == '__main__':
    unittest.main()