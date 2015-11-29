from PIL import Image
import src.binarization
import src.rotation
import src.extractor

def process(path):
    ''' Process the image at he given path '''
    image = Image.open(path)
    binary = src.binarization.binarize(image)
    rotated = src.rotation.rotate(binary)
    sums = src.extractor.get_sums(rotated)