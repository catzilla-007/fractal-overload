from image import Image


class Koch:
    def __init__(self, image: Image):
        self._image = image

    def _fractalize(self, point_a, point_b, level):
        if level == 0:
            self._image.draw_line(point_a, point_b)
        else:
            x1, y1 = point_a
            x2, y2 = point_b

            x_left = x1 + (x2 - x1) / 3
            y_left = y1 + (y2 - y1) / 3

            x_right = x2 + (x1 - x2) / 3
            y_right = y2 + (y1 - y2) / 3

            cos = 0.5
            sin = 0.866025403  # sqrt(3) / 2

            # left rotation
            x_rot = (x_right * cos) - (y_right * sin) + (x_left * (1 - cos)) + (y_left * sin)
            y_rot = (x_right * sin) + (y_right * cos) + (y_left * (1 - cos)) - (x_left * sin)

            self._fractalize((x1, y1), (x_left, y_left), level - 1)
            self._fractalize((x_left, y_left), (x_rot, y_rot), level - 1)
            self._fractalize((x_rot, y_rot), (x_right, y_right), level -1)
            self._fractalize((x_right, y_right), (x2, y2), level - 1)

    def draw(self, level: int):
        self._fractalize((800, 250), (200, 250), level)
        self._fractalize((500, 770), (800, 250), level)
        self._fractalize((200, 250), (500, 770), level)
        self._image.show_image('Koch')
