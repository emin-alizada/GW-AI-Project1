from AI_project1 import A_star


def test_normal():
    assert A_star((3, 2, 3), 2) == 2
    assert A_star((2, 5, 6, 72), 143) == 7
    assert A_star((3, 10, 15), 18) == 4
    assert A_star((3, 5), 4) == 7
    assert A_star((3, 5, 10), 18) == 6
    assert A_star((3, 5, 8, 10), 207) == 43
    assert A_star((3, 5, 9), 34) == 11
    assert A_star((3, 5), 4) == 7
    assert A_star((2, 4, 5), 8) == 4
    assert A_star((1, 4, 10, 15, 22), 181) == 19
    assert A_star((2, 13, 30, 45), 11) == 3
    assert A_star((4, 9, 24, 150), 2) == 6


def test_impossible():
    assert A_star((3, 6), 2) == -1
    assert A_star((2,), 143) == -1
    assert A_star((2, 4, 10), 141) == -1
