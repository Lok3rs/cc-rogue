from .item import Item


MAX_ITEMS_BY_TYPE = 3


class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = dict()

    def add(self, item: Item):
        items_count = sum([len(x) for x in self.items.values()])
        if items_count < self.capacity:
            if item.type in self.items:
                if len(self.items[item.type]) < MAX_ITEMS_BY_TYPE:
                    self.items[item.type].append(item)
                else:
                    adverb = "mutch" if item.type == "food " else "many"
                    return {"is_added": False, "message": f"You have too {adverb} {item.type}s in your rucksack"}
            else:
                self.items[item.type] = [item]
                
            return {"is_added": True, "message": f"You pick up the {item.name}"}
        else:
            return {"is_added": False, "message": "Your inventory is full"}

    def get_items(self):
        return self.items
