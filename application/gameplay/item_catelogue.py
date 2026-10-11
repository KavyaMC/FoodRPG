from .item import Item


class ItemCatalog:
    def __init__(self, data):
        self.items = {}

        for item_data in data.get("items", []):
            item = Item.from_dict(item_data)
            self.items[item.item_id] = item

    def get(self, item_id):
        return self.items.get(item_id)

    def get_by_name(self, item_name):
        for item in self.items.values():
            if item.item_name == item_name:
                return item

        return None

    def get_by_type(self, item_type):
        return [item for item in self.items.values() if item.item_type == item_type]

    def get_by_tag(self, tag):
        return [item for item in self.items.values() if tag in item.tags]

    def all(self):
        return list(self.items.values())
