import pytest

POSITIVE_TEST_DATA = [
    {"name": "New Object555", "data": {"color": "pink", "size": "small"}}
]
NEGATIVE_TEST_DATA = [{"data": {"color": "pink", "size": "small"}},
                      {"name": "New Object555"}
                      ]
TEST_DATA_FOR_UPDATE_OBJECT_TEST = [{"data": {"color": "white", "size": "small"}},
                                    {"name": "Updated Post Name"}
                                    ]


@pytest.mark.parametrize('data', POSITIVE_TEST_DATA)
def test_create_new_object_valid_data(create_object_endpoint, data):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_response_status_code_is_200()


@pytest.mark.parametrize('payload', NEGATIVE_TEST_DATA)
def test_create_new_object_invalid_data(create_object_endpoint, payload):
    create_object_endpoint.create_new_object(payload=payload)
    create_object_endpoint.check_response_status_code_is_not_200()


@pytest.mark.parametrize('data', POSITIVE_TEST_DATA)
def test_update_all_object_valid_data(update_all_object_endpoint, object_id, data):
    update_all_object_endpoint.update_all_object(object_id, data)
    update_all_object_endpoint.check_response_status_code_is_200()


@pytest.mark.parametrize('data', NEGATIVE_TEST_DATA)
def test_update_all_object_invalid_data(update_all_object_endpoint, object_id, data):
    update_all_object_endpoint.update_all_object(object_id, data)
    update_all_object_endpoint.check_response_status_code_is_not_200()


@pytest.mark.parametrize('data', TEST_DATA_FOR_UPDATE_OBJECT_TEST)
def test_update_part_of_object(update_part_of_object_endpoint, object_id, data):
    update_part_of_object_endpoint.update_part_of_object(object_id, data)
    update_part_of_object_endpoint.check_response_status_code_is_200()


def test_update_on_object_all_parameters_unfilled(update_part_of_object_endpoint, object_id):
    body = {
    }
    update_part_of_object_endpoint.update_part_of_object(object_id, body)
    update_part_of_object_endpoint.check_response_status_code_is_not_200()


def test_delete_an_object(delete_object_endpoint, object_id):
    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_response_status_code_is_200()
