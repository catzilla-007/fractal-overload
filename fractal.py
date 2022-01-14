from abc import ABC, abstractmethod
from image import Image


class Fractal(ABC):
    def __init__(self, image: Image):
        self._image = image

    @abstractmethod
    def _fractalize(self, point_a, point_b, level):
        pass

    @abstractmethod
    def draw(self, level):
        pass
