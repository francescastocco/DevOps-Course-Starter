import pytest
from todo_app.view_models.items_view_model import ItemsViewModel
from todo_app.data.classes.item import Item

item_1 = Item(1, "Item 1", "To Do")
item_2 = Item(2, "Item 2", "Doing")
item_3 = Item(3, "Item 3", "Done")

@pytest.fixture
def items_view_model():
    return ItemsViewModel(
        [
            item_1,
            item_2,
            item_3
        ],
        None
        )


@staticmethod
def test_to_do_items_returns_items_with_to_do_status(items_view_model: ItemsViewModel):
    #Arrange

    #Act
    to_do_items = items_view_model.to_do_items

    #Assert
    assert len(to_do_items) == 1
    assert item_1 in to_do_items

@staticmethod
def test_doing_items_returns_items_with_doing_status(items_view_model: ItemsViewModel):
    #Arrange

    #Act
    doing_items = items_view_model.doing_items

    #Assert
    assert len(doing_items) == 1
    assert item_2 in doing_items

@staticmethod
def test_done_items_returns_items_with_done_status(items_view_model: ItemsViewModel):
    #Arrange

    #Act
    done_items = items_view_model.done_items

    #Assert
    assert len(done_items) == 1
    assert item_3 in done_items