import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS


class TestExercise1205(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1205"

    def run_exercise(self, *inputs) -> list[str]:
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

    def test_discount(self):
        lines = self.run_exercise("lunes", 11)
        discount = lines[0].lower().__contains__("accede")
        self.assertTrue(discount, "The text is not specified as the exercise requires.")
        self.validateRegex(lines[0])

    def test_no_discount(self):
        lines = self.run_exercise("lunes", 2)
        self.assertEqual(lines, [])

    def test_no_discount_weekday(self):
        lines = self.run_exercise("martes", 10)
        self.assertEqual(lines, [])


if __name__ == '__main__':
    unittest.main()
