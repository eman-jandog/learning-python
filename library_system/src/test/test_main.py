from run import app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize("title, author, code, id", [
    ('Harry Potter','J. K. Rowling', 201, 1),
    ('Percy Jackson','Rick Riordan', 201, 2),
    ('A Song of Ice and Fire', 'George R. R. Martin', 201, 3),
])
def test_add_book(client, title, author, code, id):
    response = client.post('/add', data={'title': title, 'author': author})
    assert response.status_code == code
    assert response.json == {"bid": id}

def test_get_book(client):
    response = client.get('/get')
    assert response.json.get('data') == [{'bid': 1, 'title': 'Harry Potter', 'author': 'J. K. Rowling'},{'bid': 2, 'title': 'Percy Jackson', 'author': 'Rick Riordan'},{'bid': 3, 'title': 'A Song of Ice and Fire', 'author': 'George R. R. Martin'}]

@pytest.mark.parametrize("id", [
    (1),
    (2),
    (3),
])
def test_remove_book(client, id):
    response = client.delete(f'/remove/{id}')
    assert response.status_code == 200
    assert response.json == {"message": "success"}


    # [{'title': 'Harry Potter', 'author': 'J. K. Rowling'},{'title': 'Percy Jackson', 'author': 'Rick Riordan'},{'title': 'A Song of Ice and Fire', 'author': 'George R. R. Martin'}]