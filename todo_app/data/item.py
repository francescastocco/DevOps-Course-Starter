class Item:
    def __init__(self, id, name, list_id, status='To Do'):
        self.id = id
        self.name = name
        self.list_id = list_id
        self.status = status

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['id'], list['name'])