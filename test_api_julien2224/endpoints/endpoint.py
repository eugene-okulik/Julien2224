import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that status code is 200')
    def check_response_status_code_is_200(self):
        print(self.response.status_code)
        assert self.response.status_code == 200

    @allure.step('Check that status code is not 200')
    def check_response_status_code_is_not_200(self):
        print('=================================', self.response.status_code)

        assert self.response.status_code != 200
