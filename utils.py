```python
import json
import requests

def make_request(url, method, headers=None, params=None, data=None):
    """
    Function to make a request to the ToastTab APIs
    """
    if method == 'GET':
        response = requests.get(url, headers=headers, params=params)
    elif method == 'POST':
        response = requests.post(url, headers=headers, params=params, data=json.dumps(data))
    elif method == 'PUT':
        response = requests.put(url, headers=headers, params=params, data=json.dumps(data))
    elif method == 'DELETE':
        response = requests.delete(url, headers=headers, params=params)
    else:
        raise ValueError('Invalid method')

    return response.json()

def validate_response(response, expected_keys):
    """
    Function to validate the response from the ToastTab APIs
    """
    for key in expected_keys:
        if key not in response:
            raise ValueError(f'Missing key {key} in response')

    return True
```