from .entity import Entity


class Item(Entity):
    def __init__(self, x, y, type):
        if type == "key":
            character = "k"
            color = (249, 215, 28)
            name = "Key"
        super().__init__(x, y, character, color)
        self.name = name
        self.type = type
