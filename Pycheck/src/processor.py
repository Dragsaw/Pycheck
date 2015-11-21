from PIL import Image
import src.binarization
import src.rotation

def process(path):
    ''' Process the image at he given path '''
    image = Image.open(path)
    binary = src.binarization.binarize(image)
    binary.save('E:\\1.bmp')
    src.rotation.rotate(binary)