from image import Image
from koch import Koch
from hat import Hat
from peano import Peano
from inv_koch import InvKoch


width, height = 1000, 1000
black = (0, 0, 0)
white = (255, 255, 255)

fractals = [Koch, Hat, Peano, InvKoch]

for Fractal in fractals:
    for i in range(5):
        image = Image(height, width, black, white)
        fractal = Fractal(image)
        fractal.draw(i)
