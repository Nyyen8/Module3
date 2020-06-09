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
        with mock.patch('builtints.input', side_effects=[85,90,95]):
            assert avg.average() == 90
        '''This test checks '''

    def test_convert_to_months_fail(self):
        self.assertNotEqual(36, camper_age_input.convert_to_months(1))
        '''This test checks '''

if __name__ == '__main__':
    unittest.main()