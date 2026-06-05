import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_STRING_WITHOUT_COLON


class TestExercise1216(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1216"

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

    def test_replace_lower(self):
        lines = self.run_exercise(" Hola como va ", "o")

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertTrue(m1[0].__contains__("*"))
        self.assertEqual(m1[0].count("*"), 3)


    def test_replace_upper(self):
        lines = self.run_exercise(" HOLA COMO VA ", "O")

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertTrue(m1[0].__contains__("*"))
        self.assertEqual(m1[0].count("*"), 3)

    def test_replace_upper_lower_char(self):
        lines = self.run_exercise(" HOLA COMO VA ", "o")

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertTrue(m1[0].__contains__("*"))
        self.assertEqual(m1[0].count("*"), 3)

    def test_replace_lower_upper_char(self):
        lines = self.run_exercise(" hola como va ", "O")

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertTrue(m1[0].__contains__("*"))
        self.assertEqual(m1[0].count("*"), 3)

    def test_replace_not_matching_char(self):
        lines = self.run_exercise(" hola como va ", "j")

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertFalse(m1[0].__contains__("*"))
        self.assertEqual(m1[0].count("*"), 0)


if __name__ == '__main__':
    unittest.main()