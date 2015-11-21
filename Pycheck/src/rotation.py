from PIL import Image
from PIL import ImageDraw
import math

def rotate(image):
    ''' Tries to straighten the image. '''
    right_point = _find_horizontal(image)
    left_point = _find_left_point(image, right_point, image.width - 2 * image.width / 3)
    print(left_point)
    print(right_point)
    angle = math.atan((right_point[0] - left_point[0]) / (right_point[0] - left_point[0]))
    image.rotate(-angle).save("E:\\4.bmp")

def _find_horizontal(image):
    ''' Tries to find left upper right line of the table. '''
    starting_point = _find_page(image)
    line_point = _go_down(image, starting_point)
    draw = None
    while (line_point[1] > image.height / 3):
        if draw == None:
            draw = ImageDraw.Draw(image)
        draw.point([starting_point], 0)
        starting_point = _find_page(image)
        line_point = _go_down(image, starting_point)
    image.save("E:\\5.bmp")
    return line_point

def _find_page(image):
    ''' Tries to find the upper right corner of the page. '''
    step = image.width // 20
    vertical_end = image.height // 6
    horizontal_end = image.width // 3
    number_of_vertical_steps = math.ceil(vertical_end / step)
    number_of_horizontal_steps = math.ceil(horizontal_end / step)
    for i in range(1, number_of_vertical_steps):
        for j in range(1, number_of_horizontal_steps):
            x = i * step
            y = j * step
            if _check_page(image, image.width - x, y, step):
                return (image.width - x, y)

def _check_page(image, x, y, square):
    ''' Checks if page is found. '''
    step = math.ceil(square / 2)
    blacks = 0
    max_blacks = ((step * 2) ** 2) * 0.05
    for i in range(-step, step):
        for j in range(-step, step):
            if image.getpixel((x + i, y + j)) == 0:
                blacks += 1
                if (blacks > 1):
                    return False
    return True

def _go_down(image, point):
    ''' Goes down until the line. '''
    while image.getpixel(point) == 255:
        point = (point[0], point[1] + 1)
    return point

def _find_left_point(image, right_point, end_point):
    ''' Finds left end of the line. '''
    point = ()
    for i in range(-5, 5):
        point = (right_point[0] - 1, right_point[1] - i)
        if point[0] < end_point:
            return point
        if image.getpixel(point) == 0:
            break
    else:
        while image.getpixel((point[0], point[1] - 1)) == 0:
            point[1] += 1
        return point
    return _find_left_point(image, point, end_point)