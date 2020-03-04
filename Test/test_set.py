import unittest
from Src.set import Set


class MyTestCase(unittest.TestCase):
    def test_default_create_returns_empty_set(self):
        self.assertEqual([], Set().data)

    def test_create_returns_default_contents(self):
        self.assertEqual(([None] * 10), Set(size=10).data)

    def test_create_returns_correct_length(self):
        self.assertEqual(10, Set(10).getSize())

    def test_add_element_to_empty_set(self):
        # Arrange
        testset = Set()
        # Act
        testset.add(1)
        # Assert
        self.assertEqual([1], testset.data)

    def test_add_new_element_to_nonempty_set(self):
        # Arrange
        testset = Set()
        # Act
        testset.add(1)
        testset.add(2)
        # Assert
        self.assertEqual([1, 2], testset.data)

if __name__ == '__main__':
    unittest.main()
