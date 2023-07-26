from dh import rev_colex_perms


def test():

    assert rev_colex_perms(3) == [(0, 1, 2), (1, 0, 2), (0, 2, 1), (2, 0, 1), (1, 2, 0), (2, 1, 0)]
