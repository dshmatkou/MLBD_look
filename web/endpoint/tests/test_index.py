from django.test import TestCase
from pyindex import PySmallWorldIndex


class IndexTest(TestCase):

    def test_create(self):
        index = PySmallWorldIndex(2, 2)
        assert index.dimension == 2

    def test_add(self):
        index = PySmallWorldIndex(2, 2)
        index.add_item('a', [1, 2])

    def test_knn1(self):
        index = PySmallWorldIndex(2, 2)

        index.add_item('x', [10, 10])
        index.add_item('y', [0, 10])
        index.add_item('z', [10, 0])

        index.add_item('a', [0, 0])
        index.add_item('b', [0, 1])
        index.add_item('c', [1, 0])
        index.add_item('d', [1, 1])

        result1 = index.find_k_nearest(1, [0.3, 0.3])
        assert len(result1) == 1
        assert result1[0][0] == 'a'
        assert result1[0][1] == (0, 0)

        result2 = index.find_k_nearest(3, [0.3, 0.3])
        assert len(result2) == 3
        assert {result2[0][0], result2[1][0], result2[2][0]} == {'a', 'b', 'c'}
        assert {result2[0][1], result2[1][1], result2[2][1]} == {(0, 0), (0, 1), (1, 0)}
