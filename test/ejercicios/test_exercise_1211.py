import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_INT_ONLY, REGEX_FOR_STRING_WITHOUT_COLON, \
    REGEX_FOR_FLOAT_INT


class TestExercise1211(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1211"

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

    def test_range_number(self):
        lines = self.run_exercise(100, -20, 250, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, -2, -2, -2, -2, -2, 3, 3, 3, 3, 3)

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])
        m2 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[1])
        m3 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[2])
        m4 = re.findall(REGEX_FOR_INT_ONLY, lines[3])
        m5 = re.findall(REGEX_FOR_INT_ONLY, lines[4])
        m6 = re.findall(REGEX_FOR_FLOAT_INT, lines[5])

        print(lines)
        self.assertIsNotNone(m1)
        self.assertIsNotNone(m2)
        self.assertIsNotNone(m3)
        self.assertTrue(m1[0].lower().__contains__("fuera de rango"))
        self.assertTrue(m2[0].lower().__contains__("fuera de rango"))
        self.assertTrue(m3[0].lower().__contains__("fuera de rango"))

        self.assertIsNotNone(m4)
        self.assertIsNotNone(m5)
        self.assertIsNotNone(m6)
        self.assertTrue(m4[0].__contains__("-10"))
        self.assertTrue(m5[0].__contains__("5"))
        self.assertTrue(m6[0].__contains__("1.25"))

        self.validateRegex(lines[3])
        self.validateRegex(lines[4])
        self.validateRegex(lines[5])

    def test_missing_input(self):
        with self.assertRaises(StopIteration):
            self.run_exercise(5, 1, 2, 3, 4)


if __name__ == '__main__':
    unittest.main()