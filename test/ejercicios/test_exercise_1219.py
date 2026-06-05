import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch

from utils.constant import REGEX_FOR_LETTERS, REGEX_FOR_STRING_WITHOUT_COLON


class TestExercise1219(unittest.TestCase):
    MODULE_NAME = "src.ejercicios.ejercicio1219"

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

    def test_enter(self):
        lines = self.run_exercise("aqui me pongo a cantar")

        m1 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[0])
        m2 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[1])
        m3 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[2])
        m4 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[3])
        m5 = re.findall(REGEX_FOR_STRING_WITHOUT_COLON, lines[4])


        print(lines)
        self.assertIsNotNone(m1)
        self.assertEqual(m1[0], "aqui")
        self.assertEqual(m2[0], "me")
        self.assertEqual(m3[0], "pongo")
        self.assertEqual(m4[0], "a")
        self.assertEqual(m5[0], "cantar")


if __name__ == '__main__':
    unittest.main()