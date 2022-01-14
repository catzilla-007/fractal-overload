from fractal import Fractal


class Hat(Fractal):
    def _fractalize(self, point_a, point_b, level):
        if level == 0:
            self._image.draw_line(point_a, point_b)
            return

        cos = 0
        sin = 1

        x1, y1 = point_a
        x2, y2 = point_b

        x_left = x1 + (x2 - x1) / 3
        y_left = y1 + (y2 - y1) / 3

        x_right = x2 + (x1 - x2) / 3
        y_right = y2 + (y1 - y2) / 3

        # left rotation
        x_left_rot = (x_right * cos) - (y_right * sin) + (x_left * (1 - cos)) + (y_left * sin)
        y_left_rot = (x_right * sin) + (y_right * cos) + (y_left * (1 - cos)) - (x_left * sin)

        # right rotation
        x_right_rot = (x2 * cos) - (y2 * sin) + (x_right * (1 - cos)) + (y_right * sin)
        y_right_rot = (x2 * sin) + (y2 * cos) + (y_right * (1 - cos)) - (x_right * sin)

        self._fractalize((x1, y1), (x_left, y_left), level - 1)
        self._fractalize((x_left, y_left), (x_left_rot, y_left_rot), level - 1)
        self._fractalize((x_left_rot, y_left_rot), (x_right_rot, y_right_rot), level - 1)
        self._fractalize((x_right_rot, y_right_rot), (x_right, y_right), level - 1)
        self._fractalize((x_right, y_right), (x2, y2), level - 1)

    def draw(self, level):
        self._fractalize((250, 750), (750, 750), level)
        self._fractalize((750, 750), (750, 250), level)
        self._fractalize((750, 250), (250, 250), level)
        self._fractalize((250, 250), (250, 750), level)
        self._image.show_image('Hat')