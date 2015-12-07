from PIL import Image
from src.classes import Area, Number
from src.constants import HEIGHT, WIDTH

def get_sums(image):
    line = _get_sum_bottom_line(image)
    sums = _extract_rows(image, line)
    _equalize_digit_images(sums)
    return sums

def _get_sum_bottom_line(image):
    half = image.crop((0, 0, image.width // 2, image.height))
    white_lines = _get_white_lines(half)
    longest_streak = max(white_lines,key=lambda x: x.length)
    return _adjust_line(image, longest_streak.start)

def _get_white_lines(image):
    lines = []
    white_area = None
    pixels = image.load()
    for y in range(int(image.height / 2.5), image.height):
        if _is_white_row(pixels, image.width, y):
            if white_area == None:
                white_area = Area(y)
        else:
            if white_area != None:
                white_area.end = y
                lines.append(white_area)
                white_area = None
    return lines

def _is_white_row(pixels, width, row):
    blacks = 0
    limit = width * 0.01
    for x in range(0, width):
        if pixels[x, row] == 0:
            blacks += 1
        if blacks > limit:
            return False
    return True

def _adjust_line(image, line):
    width = image.width
    half = image.crop((width - width // 4, 0, width, image.height))
    pixels = half.load()
    while not _is_white_row(pixels, half.width, line):
        line += 1
    return line - 1

def _extract_rows(image, line):
    width = image.width
    section = image.crop((width - width // 6, 0, width, image.height))
    pixels = section.load()
    rows = []
    start = line
    end, area = _get_next_row(pixels, section.width, line)
    rows.append(area)
    gap = standard_gap = (area.start - end) * 0.8
    while gap >= standard_gap:
        end, area = _get_next_row(pixels, section.width, end)
        rows.append(area)
        gap = area.start - end
    top_line = rows[len(rows) - 1].start
    for row in rows:
        row.end, row.start = row.end - top_line, row.start - top_line
    rows_image = section.crop((0, top_line, section.width, line))
    return _extract_sums(_trim_excess(rows_image), rows)

def _get_next_row(pixels, width, line):
    start = line
    while not _is_white_row(pixels, width, line):
        line -= 1
    area = Area(line + 1, start)
    start = line
    while _is_white_row(pixels, width, line):
        line -= 1
    return (line, area)

def _trim_excess(image):
    x = image.width - 1
    pixels = image.load()
    while _is_white_column(pixels, image.height, x):
        x -= 1
    return image.crop((0,0,x,image.height))

def _is_white_column(pixels, height, col):
    blacks = 0
    limit = height * 0.01
    for y in range(0, height):
        if pixels[col, y] == 0:
            blacks += 1
        if blacks > limit:
            return False
    return True

def _extract_sums(image, rows):
    sums = []
    for row in rows:
        number_image = image.crop((0, row.start, image.width, row.end))
        number_digits = _break_to_digits(number_image)
        sums.append(Number(number_digits))
    return sums

def _break_to_digits(image):
    digits = []
    pixels = image.load()
    digit_length = 0
    digit_start = image.width
    for x in range(image.width - 1, 0, -1):
        if _is_white_column(pixels, image.height, x):
            if digit_length > 0:
                digits.append(image.crop((x + 1, 0, digit_start, image.height)))
            digit_length = 0
            digit_start = x
        else:
            digit_length += 1
    return digits

def _equalize_digit_images(sums):
    max_width = _get_max_width(sums)
    height = sums[0].digits[0].height
    for s in sums:
        for d in range(0, len(s.digits)):
            new_image = Image.new('1', (max_width, height), 'white')
            new_image.paste(s.digits[d], (0,0))
            s.digits[d] = new_image.resize((WIDTH, HEIGHT))

def _get_max_width(sums):
    max_width = 0
    for s in sums:
        s.digits = s.digits[3:]
        for d in s.digits:
            if d.width > max_width:
                max_width = d.width
    return max_width