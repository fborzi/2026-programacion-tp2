import importlib
import io
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS


class TestExercise1208(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1208"

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

    def test_fibonacci(self):
        lines = self.run_exercise()
        print(lines)

        first_number = lines[0]
        last_number = lines[-1]

        self.assertIsNotNone(first_number)
        self.assertIsNotNone(last_number)
        self.assertEqual(first_number, "0")
        self.assertEqual(last_number,"46368")


if __name__ == '__main__':
    unittest.main()
