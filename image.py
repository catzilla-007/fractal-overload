from helpers import create_line, blank_image, show_image


class Image:
    def __init__(self, height, width: int, background_color, line_color):
        self._width = width
        self._line_color = line_color
        self._image = blank_image(height, width, background_color)

    def translate_y(self, point=(0, 0)):
        x, y = point
        return tuple(x, self._width - y)

    def draw_line(self, start=(0, 0), end=(0, 0)):
        create_line(self._image, start, end, self._line_color, 1)

    def show_image(self, title="Image"):
        show_image(self._image)
