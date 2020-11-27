from .item import Item


class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = dict()

    def add(self, item: Item):
        items_count = sum([len(x) for x in self.items.values()])
        if items_count < self.capacity:
            if item.type in self.items:
                self.items[item.type].append(item)
            else:
                self.items[item.type] = [item]
            return f"You pick up the {item.name}"
        else:
            return "Your inventory is full"

    def get_items(self):
        return self.items
