import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_STRING_WITHOUT_COLON


class TestExercise1220(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1220"

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

    def test_cesar_two(self):
        lines = self.run_exercise("hola", "2")

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertEqual(m1[0], "jqnc")
        self.validateRegex(lines[0])

    def test_cesar_three(self):
        lines = self.run_exercise("extra", "3")

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertEqual(m1[0], "hawud")
        self.validateRegex(lines[0])


if __name__ == '__main__':
    unittest.main()