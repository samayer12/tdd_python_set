import unittest
from Src.set import Set


class SetTestCase(unittest.TestCase):

    # Arrange for all test cases
    def setUp(self):
        self.testset = Set()

    def test_default_create_returns_empty_set(self):
        self.assertEqual([], Set().data)

    def test_create_returns_default_contents(self):
        self.assertEqual(([None] * 10), Set(size=10).data)

    def test_create_returns_correct_length(self):
        self.assertEqual(10, Set(10).getSize())

    def test_add_element_to_empty_set(self):
        # Act
        self.testset.add(1)
        # Assert
        self.assertEqual([1], self.testset.data)
        self.assertEqual(1, self.testset.getSize())

    def test_add_new_element_to_nonempty_set(self):

        # Act
        self.testset.add(1)
        self.testset.add(2)
        # Assert
        self.assertEqual([1, 2], self.testset.data)
        self.assertEqual(2, self.testset.getSize())

    def test_add_existing_element_without_changing_size(self):
        # Act
        self.testset.add(1)
        self.testset.add(1)
        # Assert
        self.assertEqual([1], self.testset.data)
        self.assertEqual(1, self.testset.getSize())

if __name__ == '__main__':
    unittest.main()
