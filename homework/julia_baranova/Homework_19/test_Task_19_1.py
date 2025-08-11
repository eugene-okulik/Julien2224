import requests
import pytest


@pytest.fixture()
def new_object_id():
    body = {
        "name": "New Object",
        "data": {"color": "pink", "size": "small"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


@pytest.fixture(scope="function", autouse=True)
def start_and_end_of_each_test():
    print('before test')
    yield
    print()
    print('after test')


@pytest.fixture(scope='session', autouse=True)
def start_and_end_of_all_tests():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.mark.critical
def create_new_object():
    body = {
        "name": "New Object555",
        "data": {"color": "pink", "size": "small"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Object was not created'


@pytest.mark.parametrize('body', [{
    "data": {"color": "pink", "size": "small"}}, {
    "name": "New Object555",
}, {}])
def test_create_new_object(body):
    body = body
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, 'New object was created without required parameter "name"'


@pytest.mark.medium
def test_put_an_object(new_object_id):
    body = {
        "name": "Updated Post1",
        "data": {"color": "pink", "size": "small"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Object was not updated using put method'


def test_put_an_object_name_unfilled(new_object_id):
    body = {
        "data": {"color": "pink", "size": "small"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, 'Object was updated without "name" parameter'


def test_put_an_object_data_unfilled(new_object_id):
    body = {
        "name": "New Object555",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, 'Object was updated without "data" parameter'


def test_put_an_object_all_parameters_unfilled(new_object_id):
    body = {
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, 'Object was updated without "data" and "name" parameters'


def test_patch_name_of_object(new_object_id):
    body = {
        "name": "Updated Post Name",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Objects name was not updated using patch method'


def test_patch_data_of_object(new_object_id):
    body = {
        "data": {"color": "white", "size": "small"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Objects data was not updated using patch method'


def test_patch_on_object_all_parameters_unfilled(new_object_id):
    body = {
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, "Method patch doesn't work as expected in spec"


def test_delete_an_object(new_object_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    assert response.status_code == 200, "Object was not deleted"
