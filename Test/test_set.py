import unittest
from Src.set import Set


class SetTestCase(unittest.TestCase):

    # Arrange for all test cases
    def setUp(self):
        self.testset = Set()

    def tearDown(self):
        del self.testset

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

    def test_get_capacity_of_list(self):
        # Arrange
        self.testset = Set(size=10)
        # Act
        self.testset.add(1)
        # Assert
        self.assertEqual(9, self.testset.getCapacity())

    def test_remove_existing_element_from_set(self):
        # Arrange
        self.testset.add(3)
        # Act
        self.testset.remove(3)
        # Assert
        self.assertNotIn(3, self.testset.data)

    def test_remove_absent_element_is_ok(self):
        self.testset.remove(10)
        self.assertEquals([], self.testset.data)

if __name__ == '__main__':
    unittest.main()
