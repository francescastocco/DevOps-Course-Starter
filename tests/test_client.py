import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import mongomock
from todo_app.data.database_client import create_item

@pytest.fixture
def client():

    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        # Use the app to create a test_client that can be used in our tests.
        with test_app.test_client() as client:
            yield client


def test_index_page(client):
    create_item('Test card')
    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()
