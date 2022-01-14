from koch import Koch


class InvKoch(Koch):
    def draw(self, level):
        self._fractalize((20, 25), (80, 25), level)
        self._fractalize((80, 25), (50, 77), level)
        self._fractalize((50, 77), (20, 25), level)
        self._image.show_image(f'Inversed Koch level {level}')
