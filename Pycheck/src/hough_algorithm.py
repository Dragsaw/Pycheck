from math import cos, sin, tan, pi

def hough(image, coordinates):
    ''' Hough algorithm for detecting lines. '''
    lines = dict()
    angle = 170
    angle_equation = lambda x: round(x * tan(angle * pi / 180))
    steps = int(image.width // 2)
    while angle < 190:
        angle += 0.1
        blacks = 0
        for x in range(0, steps):
            y = angle_equation(x)
            if image.getpixel((coordinates[0] - x, coordinates[1] + y)) == 0:
                blacks += 1
        lines[blacks] = angle
    return 180 - lines[max(lines)]