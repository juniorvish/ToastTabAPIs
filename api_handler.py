```python
import requests
import json
from utils import validate_json

class APIHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        response = requests.get(self.base_url + endpoint)
        return validate_json(response.json())

    def post(self, endpoint, data):
        response = requests.post(self.base_url + endpoint, json=data)
        return validate_json(response.json())

    def put(self, endpoint, data):
        response = requests.put(self.base_url + endpoint, json=data)
        return validate_json(response.json())

    def delete(self, endpoint):
        response = requests.delete(self.base_url + endpoint)
        return validate_json(response.json())
```