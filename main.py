from image import Image
from koch import Koch
from hat import Hat
from peano import Peano
from inv_koch import InvKoch


width, height = 600, 600
black = (0, 0, 0)
white = (255, 255, 255)

fractals = [Koch, Hat, Peano, InvKoch]

for Fractal in fractals:
    for i in range(5):
        image = Image(height, width, black, white)
        fractal = Fractal(image)
        fractal.draw(i)
        # image.save_image(f'img/{type(fractal).__name__.lower()}-{i}.png')
