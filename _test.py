from discretehelpers.a import rev_colex_perms
from discretehelpers.perm import Perm


def test_perms():

    assert rev_colex_perms(3) == [(0, 1, 2), (1, 0, 2), (0, 2, 1), (2, 0, 1), (1, 2, 0), (2, 1, 0)]


def test_perm_concat():
    p_3 = Perm([2, 0, 1, 3])
    p_9 = Perm([3, 0, 1, 2])
    p_10 = Perm([1, 3, 0, 2])
    p_17 = Perm([3, 2, 0, 1])

    assert p_3 * p_9 == p_17
    assert p_9 * p_3 == p_10


def test_perm_graph():

    assert Perm([3, 0, 2, 1, 6, 4, 7, 5]).inversion_graph == {
        (0, 1, 2, 3): [(0, 1), (0, 2), (0, 3), (2, 3)],
        (4, 5, 6, 7): [(4, 5), (4, 7), (7, 6)]
    }
