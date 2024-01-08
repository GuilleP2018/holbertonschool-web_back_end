#!/usr/bin/env python3
""" Basic annotations - make multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Basic annotations - make multiplier """
    def multiply(n: float) -> float:
        """ Basic annotations - make multiplier """
        return n * multiplier
    return multiply
