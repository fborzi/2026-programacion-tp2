import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_STRING_WITHOUT_COLON


class TestExercise1217(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1217"

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

    def test_characters_finishing_cero(self):
        lines = self.run_exercise("f", "r", "a", "n", "c", "o", " ", "b", "o", "r", "z", "i", "0")

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertEqual(m1[0], "franco borzi")

    def test_characters_finishing_double_char(self):
        lines = self.run_exercise("f", "r", "a", "n", "c", "o", " ", "b", "o", "r", "z", "i", "fin")

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertEqual(m1[0], "franco borzi")


    def test_missing_input(self):
        with self.assertRaises(StopIteration):
            self.run_exercise("f", "r", "a", "n", "c")


if __name__ == '__main__':
    unittest.main()