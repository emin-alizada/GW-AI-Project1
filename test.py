from AI_project1 import A_star


def test_normal():
    assert A_star((3,2,3),2) == 2
    assert A_star((2,5,6,72),143) == 7


def test_impossible():
    assert A_star((3,6),2) == -1
    assert A_star((2),143) == -1



    



