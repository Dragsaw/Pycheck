from PIL import Image
import src.binarization
import src.rotation
import src.extractor
import src.resolver
import libs.perceptron.Test

def process(path):
    ''' Process the image at he given path '''
    image = Image.open(path)
    binary = src.binarization.binarize(image)
    rotated = src.rotation.rotate(binary)
    sums = src.extractor.get_sums(rotated)
    numbers = src.resolver.get_numbers(sums)
    for n in numbers:
        print(n)