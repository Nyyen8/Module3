"""
Program: test_average_scores.py
Author: Paul Elsea
Last Modified: 06/08/2020

The purpose of this program is to test the
functions in average_scores.py.
"""

import unittest
import unittest.mock as mock
from format_output import average_scores as avg

class FunctionTestCase(unittest.TestCase):

    def test_average_pass(self):
        with mock.patch('builtins.input', side_effect=[85,90,95]):
            assert avg.average() == 90
        '''This test checks to see if the average func works properly'''


if __name__ == '__main__':
    unittest.main()