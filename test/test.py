import unittest
from gentests import gentests, vals

import nurikabe

@gentests
class Test(unittest.TestCase):
    @vals([
        (["████",
          "████"], False),

        (["  ██",
          "████"], True),

        (["██  ",
          "████"], True),

        (["████",
          "  ██"], True),

        (["████",
          "██  "], True),

        (["  ██",
          "██  "], False),

        (["  ██  ██    ██  ██    ██",
          "████████████████████████",
          "  ██    ██    ██    ██  ",
          "  ██████  ████  ████    ",
          "██    ████  ██    ██████",
          "██████  ██  ████  ██  ██",
          "  ██  ████  ██  ██  ████",
          "  ██  ██  ████████  ██  ",
          "████  ██  ██    ██  ██  ",
          "  ██████    ██  ██████  ",
          "      ████████      ████",
          "████████    ██████████  "], True),

        (["  ██  ██    ██  ██    ██",
          "████████████████████████",
          "  ██    ██    ██    ██  ",
          "  ██████  ████  ████    ",
          "██    ████  ██    ██████",
          "██████  ██  ████  ██  ██",
          "  ██  ████  ██  ██  ████",
          "  ██  ██  ████████  ██  ",
          "████  ██  ██    ██  ██  ",
          "  ██████    ██  ██  ██  ",
          "      ████████      ████",
          "████████    ██████████  "], False)
    ])
    def test_something_else(self, board, result):
        new_board = [
            [0 if c == '  ' else 1
             for c in [line[i:i+2] for i in range(0, len(line), 2)]]
            for line in board]
        self.assertEqual(nurikabe.test(new_board), result)
