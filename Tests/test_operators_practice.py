import unittest


class OperatorsTest(unittest.TestCase):
    def test_equal(self):
        varA = 1
        varB = 2
        self.assertFalse(varA == varB)

    def test_not_equals(self):
        varA = 1
        varB = 2
        self.assertTrue(varA != varB)

    def test_greater_than(self):
        varA = 1
        varB = 2
        self.assertTrue(varB > varA)

    def test_less_than(self):
        varA = 1
        varB = 2
        self.assertTrue(varA < varB)

    def test_greater_or_equal(self):
        varA = 1
        varB = 2
        self.assertFalse(varA >= varB)

    def test_less_or_equal(self):
        varA = 1
        varB = 2
        self.assertTrue(varA <= varB)


if __name__ == '__main__':
    unittest.main()
