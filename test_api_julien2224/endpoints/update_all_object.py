import requests
import allure
from .endpoint import Endpoint


class UpdateAllObject(Endpoint):

    @allure.step("Update an object")
    def update_all_object(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        return self.response
