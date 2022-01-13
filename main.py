from image import Image
from koch import Koch

width, height = 1000, 1000

black = (0, 0, 0)
white = (255, 255, 255)

image = Image(height, width, black, white)

koch = Koch(image)

koch.draw(6)