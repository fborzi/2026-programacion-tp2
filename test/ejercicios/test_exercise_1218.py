import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_STRING_WITHOUT_COLON


class TestExercise1218(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1218"

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

    def test_capitalize(self):
        lines = self.run_exercise("harry POTTER")

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertEqual(m1[0], "Harry potter")

    def test_capitalize_space(self):
        lines = self.run_exercise(" harry POTTER ")

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertEqual(m1[0], "Harry potter")


if __name__ == '__main__':
    unittest.main()