# -*- coding: utf-8 -*-

from .context import dungeonwitch

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic Test Cases."""

    @staticmethod
    def test_absolute_truth_and_meaning():
        assert True


if __name__ == '__main__':
    unittest.main()
