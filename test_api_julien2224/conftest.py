import pytest
from .endpoints.create_object import CreateObject
from .endpoints.update_all_object import UpdateAllObject
from .endpoints.update_part_of_the_object import UpdatePartOfObject
from .endpoints.delete_object import DeleteObject


@pytest.fixture
def create_object_endpoint():
    return CreateObject()


@pytest.fixture
def update_all_object_endpoint():
    return UpdateAllObject()


@pytest.fixture
def update_part_of_object_endpoint():
    return UpdatePartOfObject()


@pytest.fixture
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def object_id(create_object_endpoint):
    payload = {"name": "New Object555", "data": {"color": "pink", "size": "small"}}
    create_object_endpoint.create_new_object(payload)
    yield create_object_endpoint.object_id
