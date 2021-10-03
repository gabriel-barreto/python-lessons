from unittest import TestCase

from main import find_absent_item

class TestIntSequence(TestCase):
    def test_should_return_1_when_receives_an_empty_list(self):
        expected = 1
        received = find_absent_item([])
        self.assertEqual(expected, received)

    def test_should_find_and_return_the_absent_value_of_sequence(self):
        expected = 4
        received = find_absent_item([2, 1, 5, 3, -3, -10, 20])
        self.assertEqual(expected, received)

    def test_should_return_1_when_receives_no_positive_values(self):
        expected = 1
        received = find_absent_item([-1, -2, -5, 0])
        self.assertEqual(expected, received)

    def test_should_return_the_bigger_item_plus_1_when_sequence_is_complete(self):
        expected = 8
        received = find_absent_item([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(expected, received)