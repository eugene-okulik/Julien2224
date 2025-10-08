import requests
import allure
from .endpoint import Endpoint


class UpdatePartOfObject(Endpoint):

    @allure.step("Update part of the object")
    def update_part_of_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        return self.response
