from random import randint, choice

def chance_roll(threshold, max_threshold):
    return randint(0, max_threshold) <= threshold

def random_cell(width, height):
    col = randint(0, width - 1)
    row = randint(0, height - 1)
    return row, col

def adjacent_cell(x, y):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dx, dy = choice(directions)
    return x + dx, y + dy
