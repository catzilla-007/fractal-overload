from koch import Koch


class InvKoch(Koch):
    def draw(self, level):
        self._fractalize((200, 250), (800, 250), level)
        self._fractalize((800, 250), (500, 770), level)
        self._fractalize((500, 770), (200, 250), level)
        self._image.show_image('Inversed Koch')
