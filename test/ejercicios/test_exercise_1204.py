import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS


class TestExercise1204(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1204"

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

    def test_odd(self):
        lines = self.run_exercise(11)
        odd = lines[0].__contains__("IMPAR")
        self.assertTrue(odd, "The text does not specified if it an odd number as it is required.")
        self.validateRegex(lines[0])

    def test_even(self):
        lines = self.run_exercise(10)
        even = lines[0].__contains__("PAR")
        self.assertTrue(even, "The text does not specified if it an even number as it is required.")
        self.validateRegex(lines[0])


if __name__ == '__main__':
    unittest.main()
