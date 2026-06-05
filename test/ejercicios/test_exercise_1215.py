import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_STRING


class TestExercise1215(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1215"

    def run_exercise(self, *inputs: str) -> list[str]:
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

    def test_vowels(self):
        lines = self.run_exercise(" Hola como va ")

        m1 = re.findall(REGEX_FOR_STRING, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertTrue(m1[0].__contains__("o"))
        self.assertTrue(m1[0].__contains__("a"))

        self.validateRegex(lines[0])

    def test_vowels_2(self):
        lines = self.run_exercise(" PARALELEPIPEDO ")

        m1 = re.findall(REGEX_FOR_STRING, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertTrue(m1[0].__contains__("a"))
        self.assertTrue(m1[0].__contains__("e"))
        self.assertTrue(m1[0].__contains__("i"))
        self.assertTrue(m1[0].__contains__("o"))

        self.validateRegex(lines[0])


if __name__ == '__main__':
    unittest.main()