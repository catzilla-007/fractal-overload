from fractal import Fractal
from geometry import rotate_left


class Koch(Fractal):
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

        cos = 0.5
        sin = 0.866025403  # sqrt(3) / 2

        x5, y5 = rotate_left((x3, y3), (x4, y4), sin, cos)

        self._fractalize((x1, y1), (x3, y3), level - 1)
        self._fractalize((x3, y3), (x5, y5), level - 1)
        self._fractalize((x5, y5), (x4, y4), level -1)
        self._fractalize((x4, y4), (x2, y2), level - 1)

    def draw(self, level: int):
        self._fractalize((800, 250), (200, 250), level)
        self._fractalize((500, 770), (800, 250), level)
        self._fractalize((200, 250), (500, 770), level)
        self._image.show_image('Koch')
