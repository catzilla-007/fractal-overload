from fractal import Fractal
from geometry import rotate_left, rotate_right


class Hat(Fractal):
    def _fractalize(self, point_a, point_b, level):
        if level == 0:
            self._image.draw_line(point_a, point_b)
            return

        x1, y1 = point_a
        x2, y2 = point_b

        x3 = x1 + (x2 - x1) / 3
        y3 = y1 + (y2 - y1) / 3

        x4 = x2 + (x1 - x2) / 3
        y4 = y2 + (y1 - y2) / 3

        cos = 0
        sin = 1

        x5, y5 = rotate_left((x3, y3), (x4, y4), sin, cos)
        x6, y6 = rotate_right((x4, y4), (x2, y2), sin, cos)

        edges = [
            ((x1, y1), (x3, y3)),
            ((x3, y3), (x5, y5)),
            ((x5, y5), (x6, y6)),
            ((x6, y6), (x4, y4)),
            ((x4, y4), (x2, y2)),
        ]

        for a, b in edges:
            self._fractalize(a, b, level - 1)

    def draw(self, level):
        self._fractalize((25, 75), (75, 75), level)
        self._fractalize((75, 75), (75, 25), level)
        self._fractalize((75, 25), (25, 25), level)
        self._fractalize((25, 25), (25, 75), level)
        self._image.show_image(f'Hat level {level}')
