

from random import randint
def randomPoint(left_top, right_bottom):
    x = randint(left_top[0], right_bottom[0])
    y = randint(left_top[1], right_bottom[1])
    return (x, y)

def randomRectangular(rectangulars):
    total_size = 0
    selected = 0
    for i, rectangular in enumerate(rectangulars):
        curr_size = abs(rectangular[0][0] - rectangular[1][0]) * (rectangular[0][1] - rectangular[1][1])
        if randint(0, curr_size + total_size) > total_size:
            selected = i
        total_size = curr_size + total_size
    return randomPoint(rectangulars[selected])