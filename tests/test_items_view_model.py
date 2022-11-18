import pytest
from todo_app.view_models.items_view_model import ItemsViewModel
from todo_app.data.item import Item

item_1 = Item(1, "Item 1", 1, "To Do")
item_2 = Item(2, "Item 2", 1, "To Do")
item_3 = Item(3, "Item 3", 1, "To Do")
item_4 = Item(4, "Item 4", 2, "Doing")
item_5 = Item(5, "Item 5", 2, "Doing")
item_6 = Item(6, "Item 6", 2, "Doing")
item_7 = Item(7, "Item 7", 3, "Done")
item_8 = Item(8, "Item 8", 3, "Done")
item_9 = Item(9, "Item 9", 3, "Done")

@pytest.fixture
def items_view_model():
    return ItemsViewModel([
            item_1,
            item_2,
            item_3,
            item_4,
            item_5,
            item_6,
            item_7,
            item_8,
            item_9
        ])


@staticmethod
def test_to_do_items_returns_items_with_to_do_status(items_view_model: ItemsViewModel):
    #Arrange

    #Act
    to_do_items = items_view_model.to_do_items

    #Assert
    assert len(to_do_items) == 3
    assert item_1 in to_do_items
    assert item_2 in to_do_items
    assert item_3 in to_do_items

@staticmethod
def test_doing_items_returns_items_with_doing_status(items_view_model: ItemsViewModel):
    #Arrange

    #Act
    doing_items = items_view_model.doing_items

    #Assert
    assert len(doing_items) == 3
    assert item_4 in doing_items
    assert item_5 in doing_items
    assert item_6 in doing_items

@staticmethod
def test_done_items_returns_items_with_done_status(items_view_model: ItemsViewModel):
    #Arrange

    #Act
    done_items = items_view_model.done_items

    #Assert
    assert len(done_items) == 3
    assert item_7 in done_items
    assert item_8 in done_items
    assert item_9 in done_items