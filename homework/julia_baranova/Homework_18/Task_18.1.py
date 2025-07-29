import requests
import json


def new_object():
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
    return response.json()['id']


def clear_object(object_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


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
    assert response.status_code == 201, 'Object was not created'
    assert response.json()['data'] == {"color": "pink", "size": "small"}, "Not all data is saved"


def create_new_object_without_name():
    body = {
        "data": {"color": "pink", "size": "small"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, 'New object was created without required parameter "name"'


def create_new_object_without_data():
    body = {
        "name": "New Object555",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, 'New object was created without required parameter "data"'


def create_new_object_all_empty_fields():
    body = {
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, 'New object was created without required parameters "name" and "data"'


def put_an_object():
    object_id = new_object()
    body = {
        "name": "Updated Post1",
        "data": {"color": "pink", "size": "small"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Object was not updated using put method'
    assert response.json()['name'] == 'Updated Post1', "Object name was not updated"
    clear_object(object_id)


def put_an_object_name_unfilled():
    object_id = new_object()
    body = {
        "data": {"color": "pink", "size": "small"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, 'Object was updated without "name" parameter'
    clear_object(object_id)


def put_an_object_data_unfilled():
    object_id = new_object()
    body = {
        "name": "New Object555",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, 'Object was updated without "data" parameter'
    clear_object(object_id)


def put_an_object_all_parameters_unfilled():
    object_id = new_object()
    body = {
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, 'Object was updated without "data" and "name" parameters'
    clear_object(object_id)


def patch_name_of_object():
    object_id = new_object()
    body = {
        "name": "Updated Post Name",
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Objects name was not updated using patch method'
    assert response.json()['name'] == 'Updated Post Name', \
        'Objects name was not updated using patch method'
    clear_object(object_id)


def patch_data_of_object():
    object_id = new_object()
    body = {
        "data": {"color": "white", "size": "small"}
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Objects data was not updated using patch method'
    assert response.json()['data'] == {"color": "white", "size": "small"}, \
        'Objects data was not updated using patch method'
    clear_object(object_id)


def patch_on_object_all_parameters_unfilled():
    object_id = new_object()
    body = {
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    )
    assert response.status_code == 400, "Method patch doesn't work as expected in spec"
    clear_object(object_id)


def delete_an_pobject():
    object_id = new_object()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200, "Object was not deleted"
