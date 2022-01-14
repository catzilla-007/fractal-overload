from helpers import create_line, blank_image, show_image


class Image:
    def __init__(self, height, width: int, background_color, line_color):
        self._height = height
        self._width = width
        self._line_color = line_color
        self._image = blank_image(height, width, background_color)

    def draw_line(self, start=(0, 0), end=(0, 0)):
        start = self._scale(start)
        end = self._scale(end)
        create_line(self._image, start, end, self._line_color, 1)

    def _scale(self, point):
        x, y = point
        x1 = (x / 100) * self._width
        y1 = (y / 100) * self._height
        return x1, y1

    def show_image(self, title="Image"):
        show_image(self._image, title)
