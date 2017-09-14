# A module for generating twisty puzzle scrambles

import random


def scramble():
    candidates = ["R", "R'", "R2", "L", "L'", "L2",
                    "U", "U'", "U2", "D", "D'", "D2",
                    "F", "F'", "F2", "B", "B'", "B2"]
    scramble = ''
    for _ in range(20):
        scramble += random.choice(candidates)
        if _ != 14:
            scramble += ' '
    return scramble
