# from .context import src
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import src.hello_world

def test_answer():
    assert func(4) == 5
    assert func(3) == 5
