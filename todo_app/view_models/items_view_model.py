class ItemsViewModel:
    def __init__(self, items):
        self._items = items
    
    @property
    def items(self):
        return self._items

    @property
    def to_do_items(self):
        return [item for item in self.items if item.status == 'To Do']

    @property
    def doing_items(self):
        return [item for item in self.items if item.status == 'Doing']
    
    @property
    def done_items(self):
        return [item for item in self.items if item.status == 'Done']