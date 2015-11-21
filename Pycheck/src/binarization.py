from PIL import Image
from PIL import ImageStat
from PIL import ImageEnhance
from PIL import ImageOps

def binarize(image):
    ''' Binarizes the image. '''
    grayscale = image.convert('L')
    equalized = ImageOps.equalize(grayscale)
    enhanced_image = _enhance(equalized)
    return _convert_to_binary(enhanced_image)

def _enhance(image):
    ''' Enhance image contrast. '''
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(2)

def _convert_to_binary(image):
    ''' Converts grayscale image to binary. '''
    mid = _get_mean(image)
    return image.point(lambda p: 0 if p < mid/2 else 255, '1')

def _get_mean(image):
    stats = ImageStat.Stat(image)
    return stats.mean[0]