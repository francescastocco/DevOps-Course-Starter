class ItemsViewModel:
    def __init__(self, items, user):
        self._items = items
        self._user = user
    
    @property
    def items(self):
        return self._items
    
    @property
    def user(self):
        return self._user

    @property
    def to_do_items(self):
        return [item for item in self.items if item.status == "To Do"]

    @property
    def doing_items(self):
        return [item for item in self.items if item.status == "Doing"]
    
    @property
    def done_items(self):
        return [item for item in self.items if item.status == "Done"]