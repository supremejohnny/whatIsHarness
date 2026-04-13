from app.math_demo import add


def test_known_bug_fixture():
    assert add(1, 1) == 4
