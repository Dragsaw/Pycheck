from PIL import Image
from PIL import ImageDraw
import src.PageNotFoundException as PageExc
from src.hough_algorithm import hough

def rotate(image):
    ''' Tries to straighten the image. '''
    _setup_module_variables(image)
    angle = _get_rotation_angle()
    print(angle)
    image.rotate(angle).save("E:\\4.bmp")

def _get_rotation_angle():
    ''' Calculates rotation angle. '''
    line_point = (-1,-1)
    x, y = image.width, 0
    while line_point == (-1, -1):
        page_point = _find_page_point(x - horizontal_step, y)
        line_point = _find_line_point(page_point)
    return hough(image, line_point)

def _find_page_point(x, y):
    ''' Searches for a page point on the image. '''
    initial_x = x
    while not is_page_point(x, y):
        if y > vertical_limit:
            raise PageExc.PageNotFoundException("Couldn't find a page on the image.")
        if x > horizontal_limit:
            x = x - horizontal_step
        else:
            y = y + vertical_step
            x = initial_x
    x -= horizontal_step * 2
    pixels[x, y] = 0
    return (x,y)

def is_page_point(x, y):
    ''' Checks if a point at given coordinates belongs to a page. '''
    if pixels[x,y] == 0:
        return False
    max_blacks = (vertical_step * horizontal_step) * 0.03
    blacks = 0
    for i in range(x - horizontal_step, x):
        for j in range(y, y + vertical_step):
            if pixels[i,j] == 0:
                blacks += 1
            if blacks >= max_blacks:
                return False
    return True

def _find_line_point(coordinates):
    ''' Searches for the line below given coordinates. '''
    x,y = coordinates
    while not _is_line_point(x, y) and y < vertical_limit:
        y += 1
    if y >= vertical_limit:
        return (-1,-1)
    return (x,y)

def _is_line_point(x, y):
    blacks = 0
    for i in range(-1, 2):
        for j in range(-1,2):
            if pixels[x + i, y + j] == 0:
                blacks += 1
            if blacks > 2:
                pixels[x, y - 4] = 0
                return True
    return False

def _setup_module_variables(imageParam):
    global vertical_limit
    global horizontal_limit
    global vertical_step
    global horizontal_step
    global pixels
    global image
    vertical_limit = imageParam.height // 4
    horizontal_limit = imageParam.width // 3
    vertical_step = vertical_limit // 10
    horizontal_step = horizontal_limit // 10
    pixels = imageParam.load()
    image = imageParam