import requests
import allure
from .endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step("Delete an object")
    def delete_object(self, object_id, headers=None):
        self.response = requests.delete(
            f'{self.url}/{object_id}',
            headers=headers
        )
        return self.response
