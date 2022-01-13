import cv2
import numpy as np


def create_rgb(rgb=(0, 0, 0)):
    return tuple(reversed(rgb))


def blank_image(width: int, height: int, rgb=(0, 0, 0)):
    image = np.zeros((height, width, 3), np.uint8)
    color = create_rgb(rgb)
    image[:] = color
    return image


def create_line(image, start_point, end_point, rgb, size):
    x1, y1 = start_point
    x2, y2 = end_point
    cv2.line(image, (round(x1), round(y1)), (round(x2), round(y2)), create_rgb(rgb), size)


def save_image(filename, image):
    cv2.imwrite(filename, image)


def show_image(image, title='Image'):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
