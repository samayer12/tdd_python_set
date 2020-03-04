import unittest
from Src.set import Set


class MyTestCase(unittest.TestCase):
    def test_default_create_returns_empty_set(self):
        self.assertEqual([], Set.create(self))

    def test_create_returns_default_contents(self):
        self.assertEqual(([None] * 10), Set.create(self, 10))

if __name__ == '__main__':
    unittest.main()
