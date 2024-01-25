from enums.hosts import BASE_URL
from http import HTTPStatus
from enums.status_codes import StatusCodes

class CustomRequester:
    base_headers = dict({"Content-Type": "application/json", "Accept": "application/json"})

    def __init__(self, session):
        self.base_url = BASE_URL,
        self.session = session

    def send_request(self,  method, endpoint, data=None, expected_status=HTTPStatus.OK, need_logging=True):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, json=data)
        if need_logging:
            self.log_request_and_response(response)
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}")
        return response

    def _update_session_headers(self, **kwargs):
        self.headers = self.base_headers.copy()
        self.headers.update(kwargs)
        self.session.headers.update(self.headers)
