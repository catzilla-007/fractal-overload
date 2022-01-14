def rotate_left(point_a, point_b, sin, cos):
    x1, y1 = point_a
    x2, y2 = point_b
    x_rot = (x2 * cos) - (y2 * sin) + (x1 * (1 - cos)) + (y1 * sin)
    y_rot = (x2 * sin) + (y2 * cos) + (y1 * (1 - cos)) - (x1 * sin)
    return x_rot, y_rot


def rotate_right(point_a, point_b, sin, cos):
    x1, y1 = point_a
    x2, y2 = point_b
    x_rot = (x2 * cos) - (y2 * sin) + (x1 * (1 - cos)) + (y1 * sin)
    y_rot = (x2 * sin) + (y2 * cos) + (y1 * (1 - cos)) - (x1 * sin)
    return x_rot, y_rot
