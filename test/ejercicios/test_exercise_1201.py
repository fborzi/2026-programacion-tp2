import io
import re
import importlib
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_FLOAT_INT


class TestExercise1201(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1201"

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

    def test_sum(self):
        lines = self.run_exercise(150, 10)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[0])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "160")
        self.validateRegex(lines[0])

    def test_subtract(self):
        lines = self.run_exercise(150, 10)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[1])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "140")
        self.validateRegex(lines[1])

    def test_multiply(self):
        lines = self.run_exercise(150, 10)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[2])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "1500")
        self.validateRegex(lines[2])

    def test_division(self):
        lines = self.run_exercise(150, 10)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[3])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "15.0")
        self.validateRegex(lines[3])

    def test_rest_division(self):
        lines = self.run_exercise(150, 10)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[4])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "0")
        self.validateRegex(lines[4])

    def test_integer_division(self):
        lines = self.run_exercise(150, 10)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[5])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "15")
        self.validateRegex(lines[5])

    def test_division_fail(self):
        lines = self.run_exercise(150, 0)
        print(lines)
        m = re.search(REGEX_FOR_FLOAT_INT, lines[0])
        print(m)
        self.assertIsNone(m)
        self.assertEqual(len(lines), 9, "Its not informed to the user that division by zero is not possible.")
        self.validateRegex(lines[3])

    def test_abs1(self):
        lines = self.run_exercise(-150, -10)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[6])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "150")
        self.validateRegex(lines[6])

    def test_abs2(self):
        lines = self.run_exercise(-150, -10)

        m = re.search(REGEX_FOR_FLOAT_INT, lines[7])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "10")
        self.validateRegex(lines[7])

if __name__ == '__main__':
    unittest.main()