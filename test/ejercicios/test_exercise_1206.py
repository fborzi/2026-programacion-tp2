import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_INT_ONLY


class TestExercise1206(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1206"

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

    def test_counter(self):
        lines = self.run_exercise(5, 1, 2, 3, 4, 5)
        m = re.search(REGEX_FOR_INT_ONLY, lines[0])
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "15")
        self.validateRegex(lines[0])

    def test_missing_input(self):
        with self.assertRaises(StopIteration):
            self.run_exercise(5, 1, 2, 3, 4)



if __name__ == '__main__':
    unittest.main()
