import unittest
from collections.abs import (Container, Sized, Iterable, Sequence)

from sorted_set import SortedSet

class TestConstruction(unittest.TestCase):

    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([1, 2, 3, 4])

    def test_with_duplicates(self):
        s = SortedSet([1, 1, 1])

    def test_from_iterable(self):
        def gen_iter():
            yield 1
            yield 2
            yield 3
            yield 4
        s = SortedSet(gen_iter())

    def test_default_empty(self):
        s = SortedSet()


class TestContainerProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([1, 2, 3])

    def test_positive_contained(self):
        self.assertTrue(1 in self.s)

    def test_negative_contained(self):
        self.assertFalse(4 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(4 not in self.s)

    def test_negative_not_container(self):
        self.assertFalse(1 not in self.s)


class TestSizedProtocol(unittest.TestCase):
    def test_zero_length(self):
        s = SortedSet()
        self.assertEqual(0, len(s))

    def test_zero_length_empty_list(self):
        s = SortedSet([])
        self.assertEqual(0, len(s))

    def test_eliminates_duplicates(self):
        s = SortedSet([1, 1, 2, 2])
        self.assertEqual(2, len(s))


class TestIterableProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([8, 2, 4, 4, 5])

    def test_iter(self):
        it = iter(self.s)
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), 4)
        self.assertEqual(next(it), 5)
        self.assertEqual(next(it), 8)
        self.assertRaises(StopIteration, lambda : next(it))

    def test_for_loop(self):
        exp = [2, 4, 5, 8]

        for expected, actual in zip(exp, self.s):
            self.assertEqual(expected, actual)


class TestSequenceProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([1, 2, 3, 4, 5])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_index_four(self):
        self.assertEqual(self.s[4], 5)

    def test_index_one_beyond_the_end(self):
        with self.assertRaises(IndexError):
            self.s[5]

    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 5)

    def test_index_minus_five(self):
        self.assertEqual(self.s[-5], 1)

    def test_index_one_before_beginning(self):
        with self.assertRaises(IndexError):
            self.s[-6]

    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedSet([1, 2, 3]))

    def test_slice_from_end(self):
        self.assertEqual(self.s[3:], SortedSet([4, 5]))

    def test_slice_middle(self):
        self.assertEqual(self.s[2:3], SortedSet([3]))

    def test_slice_beyond_range(self):
        self.assertEqual(self.s[10:], SortedSet())

    # when calling reversed method, python checks whether the object implements __reversed__ method
    # if not, it will use __getitem__ and __len__
    def test_reversed(self):
        s = reversed(SortedSet([1, 2, 3]))
        i = iter(s)
        self.assertEqual(next(i), 3)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 1)
        with self.assertRaises(StopIteration):
            next(i)

    def test_positive_index(self):
        s = SortedSet([0, 1, 2])
        self.assertEqual(s.index(2), 2)

    def test_negative_index(self):
        s = SortedSet([0, 1, 2])
        with self.assertRaises(ValueError):
            s.index(10)

    def test_count_zero(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual(0, s.count(5))

    def test_count_one(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual(1, s.count(1))

class TestReprProtocol(unittest.TestCase):
    def test_empty_set(self):
        s = SortedSet()
        self.assertEqual(repr(s), "SortedSet()")

    def test_repr_set(self):
        s = SortedSet([1, 2, 3, 4])
        self.assertEqual(repr(s), "SortedSet([1, 2, 3, 4])")


class TestEqualityProtocol(unittest.TestCase):
    def test_positive_equality(self):
        self.assertTrue(SortedSet([1, 2, 3]) == SortedSet([3, 2, 1]))

    def test_negative_equality(self):
        self.assertFalse(SortedSet([1, 2, 3]) == SortedSet([1,2]))

    def test_type_mismatch(self):
        self.assertFalse(SortedSet([1, 2, 3]) == [1, 2, 3])

    def test_identical(self):
        s = SortedSet([1, 2, 3])
        self.assertTrue(s == s)


class TestInequalityProtocol(unittest.TestCase):
    def test_positive_inequality(self):
        self.assertFalse(SortedSet([1, 2, 3]) != SortedSet([3, 2, 1]))

    def test_negative_inequality(self):
        self.assertTrue(SortedSet([1, 2, 3]) != SortedSet([1,2]))

    def test_type_mismatch(self):
        self.assertTrue(SortedSet([1, 2, 3]) != [1, 2, 3])

    def test_identical(self):
        s = SortedSet([1, 2, 3])
        self.assertFalse(s != s)


if __name__ == '__main__':
    unittest.main()
