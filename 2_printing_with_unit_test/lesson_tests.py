import os
import unittest
import subprocess
import builtins
import io
import sys

def fake_input(prompt):
    # print(prompt)
    return "jonny"

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = io.StringIO()
        self._input = builtins.input
        builtins.input = fake_input
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
        builtins.input = self._input

class AdditionTests(unittest.TestCase):

    def test_main(self):
        with Capturing() as output:
            import main
        print(output)
        self.assertEqual(output, ['Hello jonny!'])


if __name__ == '__main__':
    unittest.main()
