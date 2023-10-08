```python
from flask import Flask, render_template, request
from api_handler import handle_api_request
import utils

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        api_response = handle_api_request(request.json)
        return render_template('api_response.html', response=api_response)
    return render_template('index.html')

if __name__ == '__main__':
    utils.load_env_vars()
    app.run(debug=True)
```