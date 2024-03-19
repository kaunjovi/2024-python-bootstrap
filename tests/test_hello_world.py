from src import hello_world


def test_answer():
    assert hello_world.increment(4) == 5
    # assert hello_world.increment(3) == 5
